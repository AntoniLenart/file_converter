import tkinter as tk
from tkinter import filedialog, messagebox
from backend import converter, file_validator

def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    root.geometry(f"{width}x{height}+{x}+{y}")

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
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

center_window(250, 250)

frame = tk.Frame(root, padx=10, pady=10) 
frame.pack(anchor="center", side="top", pady=65)

tk.Label(frame, text="Wybierz format:").grid(row=0, column=0, pady=(0, 5))

format_var = tk.StringVar(value="jpeg")
formats = ["jpeg", "png", "gif", "mp3", "wav", "flac", "mp4", "mov"]
format_menu = tk.OptionMenu(frame, format_var, *formats)
format_menu.grid(row=1, column=0, pady=(0, 10))

tk.Button(frame, text="Wybierz plik", command=open_file).grid(row=2, column=0)

root.mainloop()