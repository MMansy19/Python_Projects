import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Creative Text Editor")

        # Create text widget with scrollbars
        self.text_widget = scrolledtext.ScrolledText(root, wrap="word", undo=True, autoseparators=True)
        self.text_widget.pack(expand="yes", fill="both")

        # Create a menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        # Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_widget.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_widget.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all_text)
        edit_menu.add_command(label="Clear All", command=self.clear_all_text)

        # Toolbar
        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        toolbar_btns = [
            ("Undo", self.text_widget.edit_undo),
            ("Redo", self.text_widget.edit_redo),
            ("Cut", self.cut_text),
            ("Copy", self.copy_text),
            ("Paste", self.paste_text),
            ("Select All", self.select_all_text),
            ("Clear All", self.clear_all_text),
            ("Count Words", self.count_words),
        ]
        for text, command in toolbar_btns:
            btn = tk.Button(toolbar, text=text, command=command, height=2, width=10)
            btn.pack(side=tk.LEFT, padx=2, pady=2)

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))

    def cut_text(self):
        self.text_widget.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_widget.event_generate("<<Paste>>")

    def select_all_text(self):
        if self.text_widget.compare("end-1c", "==", "1.0"):
            messagebox.showinfo("Info", "No text to select.")
        else:
            self.text_widget.tag_add(tk.SEL, "1.0", tk.END)
            self.text_widget.mark_set(tk.SE, tk.END)
            self.text_widget.see(tk.INSERT)

    def clear_all_text(self):
        self.text_widget.delete(1.0, tk.END)

    def count_words(self):
        content = self.text_widget.get(1.0, tk.END)
        words = content.split()
        num_words = len(words)
        messagebox.showinfo("Word Count", f"Total words: {num_words}")

