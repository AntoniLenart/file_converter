file_converter/
├── frontend/
│   ├── desktop_gui.py           # Interfejs desktopowy (Tkinter)
│   ├── web_interface.py         # Interfejs webowy (Flask/Django)
├── backend/
│   ├── file_validator.py        # Walidacja plików
│   ├── converter.py             # Moduł konwersji plików
│   ├── utils.py                 # Funkcje pomocnicze
├── static/                      # Pliki statyczne (CSS, JS dla wersji webowej)
├── tests/
│   ├── test_converter.py        # Testy jednostkowe
│   ├── test_validator.py
├── README.md                    # Instrukcja uruchomienia
├── requirements.txt             # Wymagania projektowe (biblioteki)
└── main.py                      # Plik startowy aplikacji

ffmpeg download https://github.com/BtbN/FFmpeg-Builds/releases
Następnie trzeba rozpakować wszystkie pliki do folderu static