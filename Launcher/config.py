from pathlib import Path

# ===============================
# Rutas principales
# ===============================

PROJECT_ROOT = Path(__file__).resolve().parent

ASSETS = PROJECT_ROOT / "assets"

IMAGES = ASSETS / "images"

ICONS = ASSETS / "icons"

THEMES = ASSETS / "themes"

# ===============================
# Recursos
# ===============================

LOGO = IMAGES / "logo.jpeg"
LOGO_TOP = IMAGES / "logo_top.jpg"
ICON_LINCE = IMAGES / "icon_lince.png"

YOUTUBE = "https://www.youtube.com/@IberOSINT"

HOMEPAGE = Path.home() / "IberOSINT" / "Resources" / "Firefox" / "homepage" / "iberosint_home.html"

TOOLS_HOMEPAGE = Path.home() / "IberOSINT" / "Resources" / "Tools" / "index.html"

RESULTS = Path.home() / "IberOSINT" / "Results"

# ===============================
# Aplicaciones
# ===============================

FIREFOX = "firefox"

TOR = "torbrowser-launcher"

# ===============================
# Colores
# ===============================

SIDEBAR_WIDTH = 230

WINDOW_WIDTH = 1400

WINDOW_HEIGHT = 900
