import os

# Lista obsługiwanych formatów
SUPPORTED_FORMATS = ['jpeg', 'png', 'gif', 'mp3', 'wav', 'flac', 'mp4', 'mov']

def validate_file(file_path):
    file_size = os.path.getsize(file_path) / (1000 * 1000)  # w MB
    file_ext = file_path.split('.')[-1].lower()
    print(file_ext)

    if file_ext not in SUPPORTED_FORMATS:
        return False, "Nieobsługiwany format pliku."

    if file_size > 200:
        return False, "Plik przekracza maksymalny rozmiar 200MB."

    return True, None
