from tkinter import filedialog, messagebox, Toplevel, Text, END
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading


class FolderSelector:
    def __init__(self, log_callback):
        self.folder_path = None
        self.observer = None
        self.log_window = None
        self.log_callback = log_callback

    #Open a dialog to select a folder
    def open_folder_dialog(self):
        folder_path = filedialog.askdirectory(title="Select a Folder")
        if folder_path:
            self.folder_path = folder_path
            self.show_log_window()
            self.start_monitoring()
        else:
            messagebox.showwarning("No Selection", "No folder was selected.")

    #Shows log window for monitoring messages
    def show_log_window(self):
        if self.log_window is None:
            self.log_window = Toplevel()
            self.log_window.title("Folder Changes Log")
            self.log_window.geometry("400x300")
            self.log_text = Text(self.log_window, state="disabled", wrap="word")
            self.log_text.pack(expand=True, fill="both")

        #log message
    def log_message(self, message):
        if self.log_window:
            self.log_text.configure(state="normal")
            self.log_text.insert(END, message + "\n")
            self.log_text.configure(state="disabled")
            self.log_text.see(END)

    #start monitoring
    def start_monitoring(self):
        if not self.folder_path:
            messagebox.showwarning("No Folder", "No folder selected for monitoring.")
            return

        if self.observer is not None:
            self.stop_monitoring()  # make sure previous observer is stopped

        event_handler = FolderChangeHandler(self.log_message)
        self.observer = Observer()
        self.observer.schedule(event_handler, self.folder_path, recursive=True)

        # Run the observer in a separate thread
        observer_thread = threading.Thread(target=self.observer.start)
        observer_thread.daemon = True
        observer_thread.start()

        self.log_callback("Monitoring started.")

    #stop monitoring
    def stop_monitoring(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.observer = None

        if self.log_window:
            self.log_window.destroy()
            self.log_window = None

        self.log_callback("Monitoring Stopped.")


class FolderChangeHandler(FileSystemEventHandler):
    def __init__(self, log_callback):
        super().__init__()
        self.log_callback = log_callback

    def on_created(self, event):
        if event.is_directory:
            self.log_callback(f"Folder Added: {event.src_path}")
        else:
            self.log_callback(f"File Added: {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            self.log_callback(f"Folder Deleted: {event.src_path}")
        else:
            self.log_callback(f"File Deleted: {event.src_path}")
