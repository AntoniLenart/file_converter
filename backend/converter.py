from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
from PIL import Image
from tkinter import filedialog as fd, messagebox
import moviepy.editor as mp
import os


def convert_image(input_file, input_format, output_format, infoLbl):
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
                infoLbl['text'] =  "Nie wybrano pliku do zapisu. Spróbuj ponownie."
            
        if user_canceled:
            infoLbl['text'] = "Zapis pliku został anulowany."
            return "anulowane"

        img.save(export_filename)    
        return export_filename
    
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Nie znaleziono pliku wejściowego.")
        return None
    except OSError as e:
        messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {e}")
        return None
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")
        return None


def convert_audio(input_file, input_format, output_format, infoLbl):
    try:
        user_canceled = False
        # print(input_file)

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        ffmpeg_dir = os.path.join(project_root, "static")
        os.environ["PATH"] += os.pathsep + ffmpeg_dir

        audio = AudioSegment.from_file(input_file, format=input_format)

        while True:
            export_filename = fd.asksaveasfilename(defaultextension=f'.{output_format}',
                                                    filetypes=[(f"{output_format.upper()} files", f"*.{output_format}")])

            if export_filename:  # Jeśli plik został wybrany
                break  # Wyjdź z pętli
            else:
                if messagebox.askyesno("Potwierdzenie", "Czy chcesz anulować zapisywanie pliku?"):
                    user_canceled = True  # Użytkownik potwierdził anulowanie
                    break
                # Nie wyświetlamy ostrzeżenia jeśli zamknięto przez X
                infoLbl["text"] = "Nie wybrano pliku do zapisu. Spróbuj ponownie."

        if user_canceled:
            infoLbl["text"] = "Zapis pliku został anulowany."
            return "anulowane"

        audio.export(export_filename, format=output_format)
        return export_filename

    except FileNotFoundError as e:
        messagebox.showerror("Błąd", f"Nie znaleziono pliku wejściowego. {e}")
        return None
    except OSError as e:
        messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {e}")
        return None
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")
        return None  

    # audio = AudioSegment.from_file(input_file)
    # output_file = f"{input_file.split('.')[0]}_converted.{output_format}"
    # audio.export(output_file, format=output_format)
    # return output_file


def convert_video(input_file, input_format, output_format, infoLbl):
    try:
        # Generate output file name based on input file name and desired format
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_converted.{output_format}"

        # Load video
        video = VideoFileClip(input_file)

        # Select codec based on format
        if output_format == "mp4":
            video.write_videofile(output_file, codec="libx264", audio_codec="aac")
        elif output_format == "mov":
            video.write_videofile(output_file, codec="mpeg4")
        else:
            messagebox.showerror("Unsupported output format")

        return output_file

    except Exception:
        messagebox.showerror("Error during video conversion:")
