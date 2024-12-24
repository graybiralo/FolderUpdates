from tkinter import filedialog, messagebox

class FolderSelector:
    def open_folder_dialog(self):
        """Open a dialog to select a folder."""
        folder_path = filedialog.askdirectory(title="Select a Folder")
        if folder_path:
            messagebox.showinfo("Folder Selected", f"Folder Path: {folder_path}")
        else:
            messagebox.showwarning("No Selection", "No folder was selected.")