from pydub import AudioSegment
from PIL import Image
from tkinter import filedialog as fd, messagebox
import moviepy.editor as mp


def convert_image(input_file, input_format, output_format):
    try:
        user_canceled = False
        img = Image.open(input_file)
        
        if input_format == 'png' and output_format == 'jpeg':
            img = img.convert('RGB')
        if input_format == 'jpeg' and output_format == 'png':
            img = img.convert('RGBA')
            
        while True:
            export_filename = fd.asksaveasfilename(defaultextension=f'.{output_format}',
                                                    filetypes=[(f"{output_format.upper()} files", f"*.{output_format}")])
            
            if export_filename:  # Jeśli plik został wybrany
                break  # Wyjdź z pętli
            else:
                # Sprawdź, czy użytkownik anulował okno dialogowe
                if messagebox.askyesno("Potwierdzenie", "Czy chcesz anulować zapisywanie pliku?"):
                    user_canceled = True  # Użytkownik potwierdził anulowanie
                    break
                # Nie wyświetlamy ostrzeżenia jeśli zamknięto przez X
                messagebox.showwarning("Ostrzeżenie", "Nie wybrano pliku do zapisu. Spróbuj ponownie.")
            
        if user_canceled:
            messagebox.showinfo("Informacja", "Zapis pliku został anulowany.")
            return "anulowane"

        img.save(export_filename)    
        return export_filename
    
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku wejściowego.")
        return None
    except OSError as e:
        messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {e}")
        return None
    except Exception as e:  # Ogólna obsługa wyjątków
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")
        return None

# def convert_audio(input_file, output_format):
#     audio = AudioSegment.from_file(input_file)
#     output_file = f"{input_file.split('.')[0]}_converted.{output_format}"
#     audio.export(output_file, format=output_format)
#     return output_file

# def convert_video(input_file, output_format):
#     video = mp.VideoFileClip(input_file)
#     output_file = f"{input_file.split('.')[0]}_converted.{output_format}"
#     video.write_videofile(output_file, codec="libx264")
#     return output_file

