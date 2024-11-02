import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from backend import converter, file_validator

def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    root.geometry(f"{width}x{height}+{x}+{y}")


def open_file():
    output_file = None
    file_path = filedialog.askopenfilename()
    
    if not file_path:  # Jeśli file_path jest pusty, użytkownik nie wybrał pliku
        messagebox.showwarning("Ostrzeżenie", "Nie wybrano żadnego pliku.")
        return  
    
    valid, message, input_format = file_validator.validate_file(file_path)
    
    if not valid:
        messagebox.showerror("Błąd", message)
        return
    
    selected_format = format_var.get()
    
    if selected_format in ['jpeg', 'png', 'gif']:
        output_file = converter.convert_image(file_path, input_format, selected_format)
    elif selected_format in ['mp3', 'wav', 'flac']:
        output_file = converter.convert_audio(file_path, input_format, selected_format)
    # else:
    #     output_file = converter.convert_video(file_path, selected_format)
    if output_file == 'anulowane':
        None
    elif output_file == 'None':
        messagebox.showinfo("Błąd", f"Wystąpił jakiś błąd. Spróbuj ponownie.") 
    elif output_file:
        messagebox.showinfo("Sukces", f"Plik został przekonwertowany: {output_file}") 


root = tk.Tk()
root.title("Konwerter plików")
root.resizable(False, False)

icon_image = Image.open('./static/icon.png')
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

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