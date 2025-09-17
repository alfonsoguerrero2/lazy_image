
from docx import Document
import os
from PIL import Image
from methods.file_systems import  extract_images_from_docx , save_images
from methods.image_processors import resize_and_pad_image
from methods.file_types import process_docx_images
import io
from docx import Document
from tkinter import Tk, Button, Label, filedialog, messagebox
import tkinter as tk

print("Lazy Image Extractor Initialized")


# --- New App Structure ---
class LazyImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lazy Image Extractor")
        self.root.geometry("500x300")

        self.selected_file = None

        self.label = tk.Label(root, text="Extract and process images from a Word document.", wraplength=400)
        self.label.pack(pady=15)

        self.file_label = tk.Label(root, text="No file selected", fg="gray")
        self.file_label.pack(pady=5)

        self.open_btn = tk.Button(root, text="Select DOCX File", command=self.select_file, height=2, width=25)
        self.open_btn.pack(pady=10)

        self.process_btn = tk.Button(root, text="Process and Save Images", command=self.process_file, height=2, width=25, state=tk.DISABLED)
        self.process_btn.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Word Document",
            filetypes=[("Word Documents", "*.docx")]
        )
        if file_path:
            self.selected_file = file_path
            file_name = os.path.basename(file_path)
            self.file_label.config(text=f"Selected: {file_name}", fg="black")
            self.process_btn.config(state=tk.NORMAL)
        else:
            self.selected_file = None
            self.file_label.config(text="No file selected", fg="gray")
            self.process_btn.config(state=tk.DISABLED)

    def process_file(self):
        if not self.selected_file:
            messagebox.showwarning("No file", "Please select a DOCX file first.")
            return
        output_folder = filedialog.askdirectory(title="Select Output Folder for Images")
        if not output_folder:
            return
        try:
            saved_paths = process_docx_images(self.selected_file, output_folder=output_folder)
            messagebox.showinfo("Success", f"Images saved to:\n" + "\n".join(saved_paths))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")


def main():
    root = tk.Tk()
    app = LazyImageApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


