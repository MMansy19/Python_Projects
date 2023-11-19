import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    
    window.title(f'My text editor - {filepath}')
    
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    
    window.title(f'My text editor - {filepath}')

# `window = tk.Tk()` creates a new instance of the Tkinter `Tk` class, which represents the main
# window of the application. This line initializes the main window and assigns it to the variable
# `window`, which can be used to configure and manipulate the window.
window = tk.Tk()
window.title("My Text Editor")
window.geometry("800x600")

txt_edit = tk.Text(window, wrap="word")
txt_edit.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

frame_buttons = tk.Frame(window, relief=tk.RAISED)
frame_buttons.grid(row=0, column=0, sticky="ns")

btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save As", command=save_file)

btn_open.pack(fill=tk.X, pady=5)
btn_save.pack(fill=tk.X, pady=5)

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

window.mainloop()
