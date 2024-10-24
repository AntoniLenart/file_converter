import tkinter as tk
from tkinter import filedialog, messagebox
from backend import converter, file_validator

def open_file():
    file_path = filedialog.askopenfilename()
    valid, message = file_validator.validate_file(file_path)
    if not valid:
        messagebox.showerror("Błąd", message)
        return
    # Przeprowadź konwersję na wybrany format
    selected_format = format_var.get()
    if selected_format in ['jpeg', 'png', 'gif']:
        output_file = converter.convert_image(file_path, selected_format)
    elif selected_format in ['mp3', 'wav', 'flac']:
        output_file = converter.convert_audio(file_path, selected_format)
    else:
        output_file = converter.convert_video(file_path, selected_format)
    messagebox.showinfo("Sukces", f"Plik został przekonwertowany: {output_file}")

root = tk.Tk()
root.title("Konwerter plików")

format_var = tk.StringVar(value="jpeg")
formats = ["jpeg", "png", "gif", "mp3", "wav", "flac", "mp4", "mov"]

tk.Label(root, text="Wybierz format:").pack()
format_menu = tk.OptionMenu(root, format_var, *formats)
format_menu.pack()

tk.Button(root, text="Wybierz plik", command=open_file).pack()

root.mainloop()
