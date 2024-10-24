import os

# Lista obsługiwanych formatów
SUPPORTED_PHOTO_FORMATS = ['jpeg', 'png', 'gif']
SUPPORTED_VIDEO_FORMATS = ['mp4', 'flac']
SUPPORTED_AUDIO_FORMATS = ['mp3', 'wav']

SUPPORTED_FORMATS = SUPPORTED_PHOTO_FORMATS + SUPPORTED_VIDEO_FORMATS + SUPPORTED_AUDIO_FORMATS


def validate_file(file_path):
    try:
        file_size = os.path.getsize(file_path) / (1024 * 1024)  # w MB
        file_ext = file_path.split('.')[-1].lower()
    except FileNotFoundError:
        return False, "Nie wybrano pliku."

    if file_ext not in SUPPORTED_FORMATS:
        return False, "Nieobsługiwany format pliku."

    if file_size > 200:
        return False, "Plik przekracza maksymalny rozmiar 200MB."

    return True, None
