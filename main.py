from tkinter import Tk, Label, Button
from folder_selector import FolderSelector

class FolderManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Manager")

        # Title
        Label(root, text="Welcome to Folder Manager", font=("Helvetica", 16)).pack(pady=10)

        # Buttons
        Button(root, text="Select Folder", command=self.select_folder, width=20).pack(pady=10)
        Button(root, text="Exit", command=root.quit, width=20).pack(pady=10)

    def select_folder(self):
        FolderSelector().open_folder_dialog()

if __name__ == "__main__":
    root = Tk()
    app = FolderManagerApp(root)
    root.mainloop()
