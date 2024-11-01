import os

# Lista obsługiwanych formatów
SUPPORTED_PHOTO_FORMATS = ['jpeg', 'png', 'gif']
SUPPORTED_VIDEO_FORMATS = ['mp4', 'flac']
SUPPORTED_AUDIO_FORMATS = ['mp3', 'wav']

SUPPORTED_FORMATS = SUPPORTED_PHOTO_FORMATS + SUPPORTED_VIDEO_FORMATS + SUPPORTED_AUDIO_FORMATS


def validate_file(file_path):
    file_size = os.path.getsize(file_path) / (1000 * 1000)  # rozmiar w MB
    file_ext = file_path.split('.')[-1].lower()


    if file_ext not in SUPPORTED_FORMATS:
        return False, "Nieobsługiwany format pliku.", file_ext

    if file_size > 200:
        return False, "Plik przekracza maksymalny rozmiar 200MB.", file_ext

    return True, None, file_ext
