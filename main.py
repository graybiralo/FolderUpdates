from tkinter import Tk, Label, Button
from folder_selector import FolderSelector


class FolderManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Manager")

        # Initialize folder selector with log callback
        self.folder_selector = FolderSelector(self.update_status)

        # Title
        Label(root, text="Welcome to Folder Manager", font=("Helvetica", 16)).pack(pady=10)

        # Buttons
        self.select_folder_button = Button(root, text="Select Folder", command=self.folder_selector.open_folder_dialog, width=20)
        self.select_folder_button.pack(pady=10)

        self.stop_monitoring_button = Button(root, text="Stop Monitoring", command=self.folder_selector.stop_monitoring, width=20)
        self.stop_monitoring_button.pack(pady=10)

        self.exit_button = Button(root, text="Exit", command=self.exit_app, width=20)
        self.exit_button.pack(pady=10)

        # Monitoring Status Label
        self.status_label = Label(root, text="Monitoring Status: Inactive", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        # Close handling for the root window
        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)


    #Updates the monitoring status label
    def update_status(self, message):
        if message == "Monitoring started.":
            self.status_label.config(text="Monitoring Status: Active")
            self.select_folder_button.config(state="disabled")
        elif message == "Monitoring Stopped.":
            self.status_label.config(text="Monitoring Status: Inactive")
            self.select_folder_button.config(state="normal")

    #Stops monitoring and exits the application
    def exit_app(self):
        self.folder_selector.stop_monitoring()
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = FolderManagerApp(root)
    root.mainloop()
