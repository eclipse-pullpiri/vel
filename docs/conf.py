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

needs_id_regex = r"^[A-Za-z0-9_]{5,}"
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
