from threading import Thread

from controllers.backend.local_api import start_server
from ui.main_window import MainWindow


if __name__ == "__main__":

    api_thread = Thread(
        target=start_server,
        daemon=True
    )

    api_thread.start()

    app = MainWindow()
    app.mainloop()
