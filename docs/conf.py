from pathlib import Path
import re

from sphinx.errors import ConfigError


project = "VEL"
author = "VEL Contributors"
release = "0.1.0"

extensions = [
    "myst_parser",
    "sphinx_needs",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 4
exclude_patterns = ["_build"]

# Pygments has no 'plantuml' lexer; the language tag is kept for correct
# semantic annotation of PlantUML diagram fences.
suppress_warnings = ["misc.highlighting_failure"]

needs_id_regex = r"^(?:STKH|FR|SEC|SAF)-VEL-\d{3}$"
needs_types = [
    {"directive": "stkh_req", "title": "Stakeholder Requirement", "prefix": "STKH-VEL-", "color": "BFD8D2", "style": "node"},
    {"directive": "feat_req", "title": "Feature Requirement", "prefix": "FR-VEL-", "color": "FEDCD2", "style": "node"},
    {"directive": "sec_req", "title": "Security Requirement", "prefix": "SEC-VEL-", "color": "F7E1AE", "style": "node"},
    {"directive": "saf_req", "title": "Safety Requirement", "prefix": "SAF-VEL-", "color": "F4C7C3", "style": "node"},
]
needs_extra_options = ["rationale", "security", "safety", "version"]
needs_extra_links = [
    {"option": "satisfies", "incoming": "satisfied by", "outgoing": "satisfies", "copy": False},
]

_DOC_PATH = Path(__file__).parent
_DOC_ID_PATTERN = re.compile(r"^((?:STKH|FR|SEC|SAF|AOU)-VEL-\d{3})(?::\s+(.*))?$")
_SCORE_DIRECTIVE_PATTERN = re.compile(r"^\.\.\s+(stkh_req|feat_req|sec_req|saf_req)::\s+(.*)$")
_SCORE_OPTION_PATTERN = re.compile(r"^\s+:(id|satisfies):\s+(.*)$")
_SECTION_RULES = {
    "Stakeholder Requirements": ("STKH", "Mapped Feature Requirements"),
    "Feature Requirements": ("FR", "Satisfies"),
    "Security Requirements": ("SEC", None),
    "Safety Requirements": ("SAF", None),
    "Assumptions of Use (AoU)": ("AOU", None),
    "이해관계자 요구사항": ("STKH", "연결 기능 요구사항"),
    "기능 요구사항": ("FR", "만족 대상"),
    "보안 요구사항": ("SEC", None),
    "안전 요구사항": ("SAF", None),
    "사용 가정(AoU)": ("AOU", None),
}
_SCORE_DIRECTIVE_PREFIX = {
    "stkh_req": "STKH",
    "feat_req": "FR",
    "sec_req": "SEC",
    "saf_req": "SAF",
}


def _extract_links(value: str) -> list[str]:
    return re.findall(r"(?:STKH|FR|SEC|SAF|AOU)-VEL-\d{3}", value)


def _parse_authoritative_requirements(path: Path) -> dict[str, dict[str, object]]:
    requirements: dict[str, dict[str, object]] = {}
    seen_ids: set[str] = set()
    current_section: str | None = None
    current_id: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        section_rule = _SECTION_RULES.get(line)
        if section_rule:
            current_section = line
            current_id = None
            continue

        id_match = _DOC_ID_PATTERN.match(line)
        if not id_match:
            if current_id and current_section:
                _, trace_label = _SECTION_RULES[current_section]
                if trace_label and line.startswith(f"{trace_label}:"):
                    requirements[current_id]["links"] = _extract_links(line.split(":", 1)[1].strip())
                    current_id = None
            continue

        requirement_id, title = id_match.groups()
        prefix = requirement_id.split("-", 1)[0]
        if requirement_id in seen_ids:
            raise ConfigError(f"{path.name}: duplicate requirement ID {requirement_id}")
        if not current_section:
            raise ConfigError(f"{path.name}: requirement {requirement_id} is outside a recognized section")

        expected_prefix, _ = _SECTION_RULES[current_section]
        if prefix != expected_prefix:
            raise ConfigError(
                f"{path.name}: requirement {requirement_id} appears in '{current_section}' but uses prefix {prefix}"
            )

        seen_ids.add(requirement_id)
        requirements[requirement_id] = {
            "category": prefix,
            "title": title or "",
            "links": [],
        }
        current_id = requirement_id

    return requirements


def _parse_score_requirements(path: Path) -> dict[str, dict[str, object]]:
    requirements: dict[str, dict[str, object]] = {}
    current: dict[str, object] | None = None
    current_requirement_id: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        directive_match = _SCORE_DIRECTIVE_PATTERN.match(raw_line)
        if directive_match:
            directive, title = directive_match.groups()
            if current is not None and current_requirement_id is None:
                raise ConfigError(f"{path.name}: directive '{current['title']}' is missing :id:")
            current = {"directive": directive, "title": title, "links": []}
            current_requirement_id = None
            continue

        if current is None:
            continue

        option_match = _SCORE_OPTION_PATTERN.match(raw_line)
        if not option_match:
            continue

        option, value = option_match.groups()
        if option == "id":
            requirement_id = value.strip()
            if requirement_id in requirements:
                raise ConfigError(f"{path.name}: duplicate requirement ID {requirement_id}")

            prefix = requirement_id.split("-", 1)[0]
            expected_prefix = _SCORE_DIRECTIVE_PREFIX[current["directive"]]
            if prefix != expected_prefix:
                raise ConfigError(
                    f"{path.name}: requirement {requirement_id} uses prefix {prefix} under {current['directive']}"
                )

            requirements[requirement_id] = {
                "category": prefix,
                "title": current["title"],
                "links": [],
            }
            current_requirement_id = requirement_id
        elif option == "satisfies":
            links = _extract_links(value)
            if current_requirement_id is None:
                raise ConfigError(f"{path.name}: :satisfies: appears before :id: in directive '{current['title']}'")
            requirements[current_requirement_id]["links"] = links

    if current is not None and current_requirement_id is None:
        raise ConfigError(f"{path.name}: directive '{current['title']}' is missing :id:")

    return requirements


def _validate_traceability(
    path: Path,
    requirements: dict[str, dict[str, object]],
    *,
    require_stakeholder_links: bool,
) -> None:
    stakeholder_ids = {req_id for req_id, req in requirements.items() if req["category"] == "STKH"}
    feature_ids = {req_id for req_id, req in requirements.items() if req["category"] == "FR"}
    reverse_traceability = {stakeholder_id: [] for stakeholder_id in stakeholder_ids}

    for feature_id in feature_ids:
        links = requirements[feature_id]["links"]
        if len(links) != 1:
            raise ConfigError(f"{path.name}: feature requirement {feature_id} must satisfy exactly one stakeholder requirement")
        stakeholder_id = links[0]
        if stakeholder_id not in stakeholder_ids:
            raise ConfigError(
                f"{path.name}: feature requirement {feature_id} satisfies unknown stakeholder requirement {stakeholder_id}"
            )
        reverse_traceability[stakeholder_id].append(feature_id)

    if not require_stakeholder_links:
        return

    for stakeholder_id in stakeholder_ids:
        links = requirements[stakeholder_id]["links"]
        if not links:
            raise ConfigError(f"{path.name}: stakeholder requirement {stakeholder_id} has no mapped feature requirement")
        for feature_id in links:
            if feature_id not in feature_ids:
                raise ConfigError(
                    f"{path.name}: stakeholder requirement {stakeholder_id} maps to unknown feature requirement {feature_id}"
                )
        if sorted(links) != sorted(reverse_traceability[stakeholder_id]):
            raise ConfigError(
                f"{path.name}: stakeholder requirement {stakeholder_id} does not match feature reverse traceability"
            )


def _validate_consistency() -> None:
    english = _parse_authoritative_requirements(_DOC_PATH / "en" / "requirements_eng.rst")
    korean = _parse_authoritative_requirements(_DOC_PATH / "ko" / "requirements_kor.rst")
    score = _parse_score_requirements(_DOC_PATH / "score" / "requirements_score.rst")

    _validate_traceability(_DOC_PATH / "en" / "requirements_eng.rst", english, require_stakeholder_links=True)
    _validate_traceability(_DOC_PATH / "ko" / "requirements_kor.rst", korean, require_stakeholder_links=True)
    _validate_traceability(_DOC_PATH / "score" / "requirements_score.rst", score, require_stakeholder_links=False)

    if set(english) != set(korean):
        missing_in_korean = sorted(set(english) - set(korean))
        missing_in_english = sorted(set(korean) - set(english))
        raise ConfigError(
            "Requirement ID mismatch between English and Korean requirements: "
            f"missing in ko={missing_in_korean}, missing in en={missing_in_english}"
        )

    score_scope = {
        req_id: req
        for req_id, req in english.items()
        if req["category"] in {"STKH", "FR", "SEC", "SAF"}
    }
    if set(score_scope) != set(score):
        missing_in_score = sorted(set(score_scope) - set(score))
        extra_in_score = sorted(set(score) - set(score_scope))
        raise ConfigError(
            "Requirement ID mismatch between authoritative requirements and S-CORE requirements: "
            f"missing in score={missing_in_score}, extra in score={extra_in_score}"
        )

    for req_id, req in score_scope.items():
        score_req = score[req_id]
        if req["links"] != korean[req_id]["links"]:
            raise ConfigError(f"Korean traceability mismatch for {req_id}")
        if req["category"] == "FR" and req["links"] != score_req["links"]:
            raise ConfigError(f"S-CORE traceability mismatch for {req_id}")


def setup(app):
    app.connect("builder-inited", lambda _app: _validate_consistency())
