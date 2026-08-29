import customtkinter as ctk
from controllers.firefox import (
    open_homepage,
    open_tools
)

from controllers.tor import open_tor
import subprocess


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, content):

        super().__init__(
            master,
            width=240,
            corner_radius=0
        )

        self.content = content

        botones = [

    ("🦊 IberoFirefox", open_homepage),

    ("🧅 IberoTOR", open_tor),

    ("🛠 IberoTOOLS", open_tools),                             

    ("🤖 Iberosint IA", self.content.show_ia_local),                               

    ("🛡 Lince", self.open_lince),                      

    ("🎓 Tutoriales", self.content.show_tutorials),

    

]
    

        for texto, comando in botones:

            boton = ctk.CTkButton(

                self,

                text=texto,

                command=comando,

                height=42,

                corner_radius=10,

                fg_color="#C62828",
                hover_color="#8E1B1B",
                
                border_width=2,
                border_color="#d8a848",

                font=("Segoe UI", 13, "bold")

            )

            boton.pack(
                fill="x",
                padx=18,
                pady=5
            )

        # -------------------------------------------------
        # INFORMACIÓN DEL PROYECTO
        # -------------------------------------------------


        ctk.CTkLabel(
            self,
            text="IberOSINT",
            font=("Segoe UI", 17, "bold"),
            text_color="white"
        ).pack(pady=(20,0))

        ctk.CTkLabel(
            self,
            text="Versión 1.0",
            font=("Segoe UI", 13),
            text_color="#b0b0b0"
        ).pack(pady=(4,8))

        ctk.CTkLabel(
            self,
            text='Transformando información\nen inteligencia.',
            justify="center",
            font=("Segoe UI", 11, "italic"),
            text_color="#8a8a8a"
        ).pack()

        ctk.CTkLabel(
            self,
            text="© 2026",
            font=("Segoe UI", 11),
            text_color="#666666"
        ).pack(pady=(8,8))
            
    def open_lince(self):
        subprocess.Popen(
            ["python3", "/home/iberosint/IberOSINT/Lince/app.py"],
            cwd="/home/iberosint/IberOSINT/Lince"
        )       

