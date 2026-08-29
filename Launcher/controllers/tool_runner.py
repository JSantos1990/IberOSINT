import os
import subprocess
import webbrowser

from controllers.tool_registry import TOOLS

def get_workdir(command: str) -> str:
    """
    Devuelve el directorio desde el que conviene ejecutar
    la herramienta.
    """

    parts = command.split()

    if not parts:
        return ""

    # Caso 1: ejecutable absoluto
    if parts[0].startswith("/"):
        return os.path.dirname(parts[0])

    # Caso 2: python3 script.py
    if parts[0].startswith("python") and len(parts) > 1:

        script = parts[1]

        if script.startswith("/"):
            return os.path.dirname(script)

    return ""


def run_tool(tool_id: str, params=None) -> bool:

    if params is None:
        params = {}

    tool = TOOLS.get(tool_id)

    if tool is None:

        print(f"[ToolRunner] '{tool_id}' no registrada.")
        return False

    # -----------------------------------------------------------------

    # Compatibilidad con el registry antiguo
    # (si el valor es simplemente una cadena)

    if isinstance(tool, str):

        command = tool

        # ---------------------------------
        # Parámetros para herramientas
        # ---------------------------------

        if tool_id == "sherlock":

            username = params.get("username")

            if username:

                command = f"{command} {username}"

        try:

            print(f"[DEBUG] Ejecutando comando: {command}")

            workdir = get_workdir(command)

            subprocess.Popen(
                [
                    "/usr/bin/gnome-terminal",
                    "--",
                    "/home/iberosint/IberOSINT/Launcher/scripts/launcher_env.sh",
                    workdir,
                    command,
                ]
            )

            print(f"[ToolRunner] Ejecutando '{tool_id}'")

            return True

        except Exception as error:

            print(error)

            return False

    # -----------------------------------------------------------------

    tool_type = tool.get("type")

    command = tool.get("command")

    status = tool.get("status", "ready")

    # -----------------------------------------------------------------

    if status != "ready":

        print(f"[ToolRunner] {tool['name']} disponible en IberoTools v2.0")

        return False

    # -----------------------------------------------------------------

    try:

        # ---------------- GUI ----------------

        if tool_type == "gui":

            subprocess.Popen(command, shell=True)

        # ------------- TERMINAL -------------

        elif tool_type == "terminal":

            print(f"[DEBUG] Ejecutando comando: {command}")

            workdir = get_workdir(command)

            subprocess.Popen(
                [
                    "/usr/bin/gnome-terminal",
                    "--",
                    "/home/iberosint/IberOSINT/Launcher/scripts/launcher_env.sh",
                    workdir,
                    command,
                ]
            )

        # ---------------- WEB ----------------

        elif tool_type == "web":

            subprocess.Popen(command, shell=True)

            if tool.get("url"):

                webbrowser.open(tool["url"])

        else:

            print(f"[ToolRunner] Tipo desconocido: {tool_type}")

            return False

        print(f"[ToolRunner] Ejecutando '{tool['name']}'")

        return True

    except Exception as error:

        print(error)

        return False