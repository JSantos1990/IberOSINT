"""
Registro central de herramientas de IberoTools.
"""

TOOLS = {

    # =====================================================
    # OSINT
    # =====================================================

    "spiderfoot": "/snap/bin/spiderfoot",

    "sherlock": "/home/iberosint/.local/bin/sherlock",

    "maigret": "/home/iberosint/.local/bin/maigret --help",

    "holehe": "/home/iberosint/.local/bin/holehe --help",

    "h8mail": "/home/iberosint/.local/bin/h8mail --help",

    "theHarvester": "/home/iberosint/.local/bin/theHarvester -h",

    "recon-ng": "/home/iberosint/Iberosint_herramientas/osint/recon-ng/recon-ng",

    "phoneinfoga": "/home/iberosint/Iberosint_herramientas/osint/phoneinfoga/phoneinfoga --help",

    "metagoofil": "python3 /home/iberosint/Iberosint_herramientas/osint/metagoofil/metagoofil.py --help",

    "photon": "python3 /home/iberosint/Iberosint_herramientas/osint/Photon/photon.py",

    "gitdumper": {
    "name": "GitDumper",
    "type": "terminal",
    "command": "/home/iberosint/Iberosint_herramientas/osint/gittools/Dumper/gitdumper.sh --help"
    },

    "gitextractor": {
        "name": "GitExtractor",
        "type": "terminal",
        "command": "/home/iberosint/Iberosint_herramientas/osint/gittools/Extractor/extractor.sh"
    },

    "gitfinder": {
    "name": "GitFinder",
    "type": "terminal",
    "command": "cd /home/iberosint/Iberosint_herramientas/osint/gittools/Finder && python3 gitfinder.py"
    },

    "gitleaks": "/home/iberosint/Iberosint_herramientas/osint/gitleaks/gitleaks",

    "trufflehog": "/home/iberosint/Iberosint_herramientas/osint/trufflehog/trufflehog",

    # =====================================================
    # RECON
    # =====================================================

    "amass": "/snap/bin/amass",

    "bbot": "/home/iberosint/.local/bin/bbot",

    "subfinder": "/home/iberosint/go/bin/subfinder",

    "assetfinder": "/home/iberosint/go/bin/assetfinder --help",

    "alterx": "/home/iberosint/Iberosint_herramientas/recon/alterx/alterx",

    "asnmap": "/home/iberosint/Iberosint_herramientas/recon/asnmap/asnmap",

    "cdncheck": "/home/iberosint/Iberosint_herramientas/recon/cdncheck/cdncheck",

    "uncover": "/home/iberosint/Iberosint_herramientas/recon/uncover/uncover",

    "chaos": {
    "name": "Chaos Client",
    "type": "terminal",
    "command": "/home/iberosint/Iberosint_herramientas/recon/chaos/chaos-client"
    },

    "dnsx": "/home/iberosint/go/bin/dnsx",

    

    # =====================================================
    # WEB
    # =====================================================

    "katana": "/home/iberosint/go/bin/katana",

    "httpx": "/home/iberosint/go/bin/httpx",

    "gospider": {
    "name": "GoSpider",
    "type": "terminal",
    "command": "/home/iberosint/Iberosint_herramientas/web/gospider/gospider_v1.1.6_linux_x86_64/gospider --help"
    },

    "aquatone": "/home/iberosint/Iberosint_herramientas/web/aquatone/aquatone --help",

    "zap": "/opt/zaproxy/zap.sh",

    

    # =====================================================
    # VULNERABILIDADES
    # =====================================================

    "nuclei": "/home/iberosint/Iberosint_herramientas/vulnerabilidades/nuclei/nuclei",

    "nikto": "perl /home/iberosint/Iberosint_herramientas/vulnerabilidades/nikto/program/nikto.pl -Help",

    # =====================================================
    # NETWORK
    # =====================================================

    "naabu": "/home/iberosint/Iberosint_herramientas/network/naabu/naabu",

    "rustscan": "/home/iberosint/Iberosint_herramientas/web/eyewitness/rustscan",

    "tlsx": "/home/iberosint/Iberosint_herramientas/network/tlsx/tlsx --help",

    "mapcidr": "/home/iberosint/Iberosint_herramientas/network/mapcidr/mapcidr",

    # =====================================================
    # CLOUD
    # =====================================================

    "scoutsuite": "scout --help",

    "prowler": "/home/iberosint/.local/bin/prowler",

    "cloudfox": {
    "name": "CloudFox",
    "type": "terminal",
    "command": "/home/iberosint/go/bin/cloudfox"
    },


    # =====================================================
    # DEVSECOPS
    # =====================================================

    "trivy": "/home/iberosint/Iberosint_herramientas/security/trivy/trivy",

    "syft": "/home/iberosint/Iberosint_herramientas/security/syft/syft",

    "grype": "/home/iberosint/Iberosint_herramientas/security/grype/grype",

    "kics": "/home/iberosint/Iberosint_herramientas/security/kics/kics",

    "sops": {
    "name": "SOPS",
    "type": "terminal",
    "command": "/home/iberosint/Iberosint_herramientas/security/sops/sops --help"
    },

    "steampipe": {
    "name": "Steampipe",
    "type": "terminal",
    "command": "/home/iberosint/Iberosint_herramientas/cloud/steampipe/steampipe"
    },

    "semgrep": {
    "name": "Semgrep",
    "type": "terminal",
    "command": "/home/iberosint/.local/bin/semgrep"
    },

    "cosign": {
    "name": "Cosign",
    "type": "terminal",
    "command": "/home/iberosint/go/bin/cosign"
    },

    # =====================================================
    # ACTIVE DIRECTORY
    # =====================================================

    "secretsdump": {
    "name": "SecretsDump",
    "type": "terminal",
    "command": "/home/iberosint/.local/bin/secretsdump.py"
    },

    "psexec": {
        "name": "PsExec",
        "type": "terminal",
        "command": "/home/iberosint/.local/bin/psexec.py"
    },

    "wmiexec": {
        "name": "WMIExec",
        "type": "terminal",
        "command": "/home/iberosint/.local/bin/wmiexec.py"
    },

    "getuserspns": {
        "name": "GetUserSPNs",
        "type": "terminal",
        "command": "/home/iberosint/.local/bin/GetUserSPNs.py"
    },

    "lookupsid": {
        "name": "LookupSID",
        "type": "terminal",
        "command": "/home/iberosint/.local/bin/lookupsid.py"
    },

    "ntlmrelayx": {
        "name": "NTLMRelayX",
        "type": "terminal",
        "command": "/home/iberosint/.local/bin/ntlmrelayx.py --help"
    },

    "netexec": "/home/iberosint/.local/bin/netexec",

    "enum4linux-ng": "/home/iberosint/.local/bin/enum4linux-ng",

    "certipy": "/home/iberosint/.local/bin/certipy",

    # =====================================================
    # UTILITIES
    # =====================================================

    "notify": "/home/iberosint/Iberosint_herramientas/utilities/notify/notify",

    "interactsh-client": {
    "name": "Interactsh Client",
    "type": "terminal",
    "command": "/home/iberosint/Iberosint_herramientas/utilities/interactsh/interactsh-client --help"
    },

    "nc": "/usr/bin/nc"
}


