# ==========================================================
# SESIÓN DE IBEROSINT AI
# ==========================================================

# ==========================================================
# PERFILES DISPONIBLES
# ==========================================================

PROFILE_GENERAL = "general"

PROFILE_OSINT = "osint_investigator"

PROFILE_THREAT = "threat_analyst"

PROFILE_DFIR = "incident_responder"

PROFILE_PENTEST = "pentester"

PROFILE_MALWARE = "malware_analyst"

PROFILE_EMAIL = "email_investigator"

PROFILE_IOC = "ioc_analyst"

PROFILE_CVE = "cve_analyst"

PROFILE_DORKS = "dorks_specialist"

PROFILE_TRANSLATOR = "translator"

PROFILE_REPORTING = "reporting_assistant"

PROFILE_SHODAN = "shodan_specialist"

_active_profile = PROFILE_GENERAL


def get_profile():
    return _active_profile


def set_profile(profile):
    global _active_profile
    _active_profile = profile