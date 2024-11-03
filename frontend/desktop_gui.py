import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from backend import converter, file_validator

# Global variables to store file path and input format
file_path = None
input_format = None
output_file = None


def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")


def open_file():
    global file_path, input_format
    file_path = filedialog.askopenfilename()

    if not file_path:
        messagebox.showwarning("Ostrzeżenie", "Nie wybrano żadnego pliku.")
        return

    valid, message, input_format = file_validator.validate_file(file_path)

    if not valid:
        messagebox.showerror("Błąd", message)
        return

    # Enable formats based on the file type
    photo_formats = ["png", "jpg", "jpeg"]
    audio_formats = ["mp3", "wav", "flac"]
    movie_formats = ["mp4", "mov"]
    if input_format in photo_formats:
        enable_option_menu(photo_formats)
    elif input_format in audio_formats:
        enable_option_menu(audio_formats)
    elif input_format in movie_formats:
        enable_option_menu(movie_formats)


def save_file():
    global file_path, input_format, output_file
    if not file_path or not input_format:
        messagebox.showwarning("Ostrzeżenie", "Nie wybrano pliku do konwersji.")
        return

    selected_format = format_var.get()

    if selected_format in ['jpeg', 'png', 'gif']:
        output_file = converter.convert_image(file_path, input_format, selected_format)
    elif selected_format in ['mp3', 'wav', 'flac']:
        output_file = converter.convert_audio(file_path, input_format, selected_format)
    elif selected_format in ['mp4', 'mov']:
        converter.convert_video(file_path, input_format, selected_format)

    if output_file == 'anulowane':
        pass
    elif output_file == 'None':
        messagebox.showinfo("Błąd", f"Wystąpił jakiś błąd. Spróbuj ponownie.")
    elif output_file:
        messagebox.showinfo("Sukces", f"Plik został przekonwertowany: {output_file}")


def enable_option_menu(formats):
    # Clear existing options and update with the new formats
    format_menu['menu'].delete(0, 'end')
    for fmt in formats:
        format_menu['menu'].add_command(label=fmt, command=tk._setit(format_var, fmt))  # access to values
    format_var.set(formats[0])
    format_menu.config(state='normal')


root = tk.Tk()
root.title("Konwerter plików")
root.resizable(False, False)

icon_image = Image.open('./static/icon.png')
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

center_window(300, 300)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(anchor="center", side="top", pady=65)

format_var = tk.StringVar(value="Wybierz format")
format_menu = tk.OptionMenu(frame, format_var, "")
format_menu.grid(row=0, column=1, pady=(0, 10))
format_menu.config(state='disabled')  # Disable until a file is selected

fileBtn = tk.Button(frame, text="Wybierz plik", command=open_file)
fileBtn.grid(row=0, column=0, pady=(0, 10))

downloadBtn = tk.Button(frame, text="Pobierz", command=save_file)
downloadBtn.grid(row=1, column=0, pady=(0, 10))

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack(side="right", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

labelFrame = tk.Frame(canvas)
labelFrame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=labelFrame, anchor="nw")

infoLbl = tk.Label(labelFrame, text="To jest bardzo długi tekst, który powinien "
                                    "się zawijać i być możliwy do przewinięcia "
                                    "w razie potrzeby. " * 5,
                   wraplength=180, justify="left")
infoLbl.pack(fill="both", expand=True)

root.mainloop()
