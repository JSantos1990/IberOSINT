from pathlib import Path


# ==========================================================
# RUTAS
# ==========================================================

BASE_PATH = Path(__file__).resolve().parent.parent

CORE_PATH = BASE_PATH / "Prompts" / "Core"

MODULES_PATH = BASE_PATH / "Prompts" / "Modules"

# ==========================================================
# PERFILES OPERATIVOS
# ==========================================================

PROFILES = {

    "general": [],

    "osint_investigator": [

        "osint",
        "threat_intelligence"

    ],

    "email_investigator": [

    "email"

    ],

    "ioc_analyst": [

    "threat_intelligence",
    "ioc"

    ],

    "cve_analyst": [

    "threat_intelligence",
    "cve"

    ],

    "dorks_specialist": [

        "dorks"

    ],

    "translator": [

        "translator"

    ],

    "reporting_assistant": [

        "reporting"

    ],

    "shodan_specialist": [

        "osint",
        "shodan"

    ],

        "incident_responder": [

            "dfir",
            "threat_intelligence"

        ],

        "pentester": [

            "pentesting"

        ],

        "malware_analyst": [

            "malware"

        ]

}


# ==========================================================
# CARGAR UN ARCHIVO
# ==========================================================

def load_prompt(filename):

    file = CORE_PATH / filename

    with open(file, "r", encoding="utf-8") as f:

        return f.read()


# ==========================================================
# CONSTRUIR PROMPT BASE
# ==========================================================

def build_core():

    partes = [

        load_prompt("core_base.txt"),

        load_prompt("core_personality.txt"),

        load_prompt("core_style.txt"),

        load_prompt("core_methodology.txt")

    ]

    return "\n\n".join(partes)

# ==========================================================
# CARGAR MÓDULOS
# ==========================================================

def load_module(filename):

    file = MODULES_PATH / filename

    with open(file, "r", encoding="utf-8") as f:

        return f.read()
    
# ==========================================================
# CONSTRUIR CONTEXTO OPERATIVO
# ==========================================================

def build_context(modules=None):

    if modules is None:

        modules = []

    contexto = build_core()

    for module in modules:

        contexto += "\n\n"

        contexto += load_module(f"module_{module}.txt")

    return contexto

# ==========================================================
# CONTEXTO POR PERFIL
# ==========================================================

def build_profile(profile):

    modules = PROFILES.get(profile, [])

    return build_context(modules)