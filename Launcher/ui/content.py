from ui.pages.workspace import show_workspace_page
from ui.pages.tor import show_tor_page
from ui.pages.home import show_home_page
from ui.pages.ia_local import show_ia_local_page
from ui.pages.tutorials import show_tutorials_page

from controllers.system_check import check_system
import customtkinter as ctk

class Content(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack_propagate(False)
        self.show_home()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_home(self):
        show_home_page(self)

    def show_workspace(self):
        show_workspace_page(self)

    def show_system_status(self):
        self.clear()
        ctk.CTkLabel(self,text='Estado del Sistema',font=('Segoe UI',30,'bold')).pack(pady=(40,20))
        box=ctk.CTkTextbox(self,width=700,height=350,font=('Consolas',16))
        box.pack(pady=10)
        box.insert('1.0',check_system())
        box.configure(state='disabled')

    def show_tor(self):
        show_tor_page(self)

    def show_ia_local(self):
        show_ia_local_page(self)

    def show_tutorials(self):
        show_tutorials_page(self)
