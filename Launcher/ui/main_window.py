import customtkinter as ctk
from PIL import Image, ImageTk
from utils.tooltip import ToolTip

from ui.sidebar import Sidebar
from ui.content import Content

import config


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("IberOSINT")

        icon = ImageTk.PhotoImage(
            Image.open(config.ICON_LINCE)
        )

        self.iconphoto(False, icon)

        self._icon = icon
            
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==========================
        # SIDEBAR
        # ==========================

        sidebar = ctk.CTkFrame(
            self,
            width=config.SIDEBAR_WIDTH,
            corner_radius=0
        )

        sidebar.grid(row=0, column=0, sticky="ns")

        # ==========================
        # LOGO
        # ==========================

        logo = ctk.CTkImage(
            light_image=Image.open(config.LOGO),
            dark_image=Image.open(config.LOGO),
            size=(170, 170)
        )

        logo_button = ctk.CTkButton(
            sidebar,
            image=logo,
            text="",
            width=170,
            height=170,
            fg_color="transparent",
            hover_color="#2b2b2b",
            border_width=0,
            corner_radius=0,

            cursor="hand2",

            command=self.go_home
        )

        logo_button.pack(pady=(25, 30))

        ToolTip(
            logo_button,
            "🏠 Volver al Inicio"
)

        # ============================================
        # PLACA CORPORATIVA
        # ============================================

        brand = ctk.CTkFrame(
            sidebar,
            fg_color="#242424",
            corner_radius=12
        )

        brand.pack(
            fill="x",
            padx=18,
            pady=(0, 10)
        )

        # Línea corporativa

        ctk.CTkFrame(
            brand,
            height=3,
            fg_color="#d8a848",
            corner_radius=10
        ).pack(
            fill="x",
            padx=18,
            pady=(10, 8)
        )

        # Título

        ctk.CTkLabel(
            brand,
            text="CENTRO DE\nINTELIGENCIA",
            justify="center",
            font=("Segoe UI", 18, "bold")
        ).pack()

        # Versión

        ctk.CTkLabel(
            brand,
            text="v1.0 DEV",
            text_color="#bbbbbb",
            font=("Segoe UI", 13, "bold")
        ).pack(pady=(8, 1))

        # Build

        ctk.CTkLabel(
            brand,
            text="Build 2026.07",
            text_color="#808080",
            font=("Segoe UI", 11)
        ).pack(pady=(0, 10))

        # ==========================
        # CONTENT
        # ==========================

        self.content = Content(self)

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=25,
            pady=25
        )

        # ==========================
        # SIDEBAR MENU
        # ==========================

        menu = Sidebar(sidebar, self.content)

        menu.pack(fill="x", pady=10)

    def go_home(self):
        self.content.show_home()

