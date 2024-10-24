from pydub import AudioSegment
from PIL import Image
import moviepy.editor as mp


def convert_image(input_file, output_format):
    img = Image.open(input_file)
    output_file = f"{input_file.split('.')[0]}_converted.{output_format}"
    img.save(output_file)
    return output_file


def convert_audio(input_file, output_format):
    audio = AudioSegment.from_file(input_file)
    output_file = f"{input_file.split('.')[0]}_converted.{output_format}"
    audio.export(output_file, format=output_format)
    return output_file


def convert_video(input_file, output_format):
    video = mp.VideoFileClip(input_file)
    output_file = f"{input_file.split('.')[0]}_converted.{output_format}"
    video.write_videofile(output_file, codec="libx264")
    return output_file
