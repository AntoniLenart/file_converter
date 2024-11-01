from pydub import AudioSegment
from PIL import Image
from tkinter import filedialog as fd
import moviepy.editor as mp

def convert_image(input_file, input_format, output_format):
    img = Image.open(input_file)
    
    if input_format == 'png' and output_format == 'jpeg':
        img = img.convert('RGB')
    if input_format == 'jpeg' and output_format == 'png':
        img = img.convert('RGBA')
        
    export_filename = fd.asksaveasfilename(defaultextension=f'{output_format}')
    img.save(export_filename)
    
    return export_filename

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
