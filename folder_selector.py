from tkinter import filedialog, messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FolderSelector:
    def __init__(self, status_callback, log_callback):
        self.folder_path = None
        self.observer = None
        self.status_callback = status_callback
        self.log_callback = log_callback

    def open_folder_dialog(self):
        """Open a dialog to select a folder."""
        folder_path = filedialog.askdirectory(title="Select a Folder")
        if folder_path:
            self.folder_path = folder_path
            self.log_callback(f"Selected Folder: {self.folder_path}")
            self.status_callback("Inactive")
        else:
            messagebox.showwarning("No Selection", "No folder was selected.")

    def start_monitoring(self):
        """Start monitoring the selected folder."""
        if not self.folder_path:
            messagebox.showwarning("No Folder", "No folder selected for monitoring.")
            return

        if self.observer is not None:
            messagebox.showinfo("Monitoring", "Monitoring is already active.")
            return

        event_handler = FolderChangeHandler(self.log_callback)
        self.observer = Observer()
        self.observer.schedule(event_handler, self.folder_path, recursive=True)
        self.observer.start()

        self.status_callback("Active")
        self.log_callback("Monitoring started.")

    def stop_monitoring(self):
        """Stop monitoring the folder."""
        if self.observer and self.observer.is_alive():
            self.observer.stop()
            self.observer.join()
        self.observer = None

        self.status_callback("Inactive")
        self.log_callback("Monitoring stopped.")


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
