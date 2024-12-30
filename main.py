from tkinter import Tk, Label, Button, Text, Scrollbar, VERTICAL, END, DISABLED, NORMAL 
from folder_selector import FolderSelector


class FolderManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Manager")

        # Initialize folder selector with status and log callbacks
        self.folder_selector = FolderSelector(self.update_status, self.log_message)

        # Title
        Label(root, text="Welcome to Folder Manager", font=("Helvetica", 16)).pack(pady=10)

        # Buttons
        self.select_folder_button = Button(root, text="Select Folder", command=self.folder_selector.open_folder_dialog, width=20)
        self.select_folder_button.pack(pady=5)

        self.start_monitoring_button = Button(root, text="Start Monitoring", command=self.start_monitoring, width=20, state="disabled")
        self.start_monitoring_button.pack(pady=5)

        self.stop_monitoring_button = Button(root, text="Stop Monitoring", command=self.stop_monitoring, width=20, state="disabled")
        self.stop_monitoring_button.pack(pady=5)

        self.exit_button = Button(root, text="Exit", command=self.exit_app, width=20)
        self.exit_button.pack(pady=5)

        # Monitoring Status Label
        self.status_label = Label(root, text="Monitoring Status: Inactive", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        # Log Display
        self.log_text = Text(root, height=15, wrap="word", state=DISABLED)
        self.log_text.pack(padx=10, pady=10, fill="both", expand=True)

        # Scrollbar
        self.scrollbar = Scrollbar(root, orient=VERTICAL, command=self.log_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.log_text.config(yscrollcommand=self.scrollbar.set)

        # Close handling for the root window
        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)



    #Updates the monitoring status label
    def update_status(self, message):
        self.status_label.config(text=f"Monitoring Status: {message}")
        if message == "Active":
            self.start_monitoring_button.config(state="disabled")
            self.stop_monitoring_button.config(state="normal")
        elif message == "Inactive":
            self.start_monitoring_button.config(state="normal")
            self.stop_monitoring_button.config(state="disabled")


    #Logs messages to the log text area.
    def log_message(self, message):
        self.log_text.config(state=NORMAL)
        self.log_text.insert(END, message + "\n")
        self.log_text.config(state=DISABLED)
        self.log_text.see(END)


    #Starts monitoring the selected folder
    def start_monitoring(self):
        self.folder_selector.start_monitoring()

    # Stops monitoring 
    def stop_monitoring(self):
        self.folder_selector.stop_monitoring()
        
    # exits the application
    def exit_app(self):
        self.folder_selector.stop_monitoring()
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = FolderManagerApp(root)
    root.mainloop()
