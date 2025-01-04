# TikTok Auto Liker & Commenter

## Opis
Ten skrypt automatycznie loguje się na TikTok, przegląda posty na określonym profilu, polubia je oraz dodaje komentarz do nowych filmów. Skrypt jest napisany w Pythonie i używa narzędzia Selenium do automatyzacji przeglądarki.

## Wymagania
1. **Python 3.x** – Upewnij się, że masz zainstalowaną wersję Pythona 3.x.
2. **Biblioteki**:
   - Selenium
   - WebDriver-Manager

## Instrukcja instalacji i uruchomienia

### Krok 1: Pobierz pliki
Pobierz lub sklonuj folder zawierający skrypt `kodzik.py`, plik `.bat` oraz ten plik README.

### Krok 2: Instalacja wymaganych bibliotek
Użyj poniższego pliku `.bat` do automatycznego zainstalowania wymaganych bibliotek oraz uruchomienia skryptu:
1. Kliknij dwukrotnie na `install_and_run.bat`.
2. Plik ten zainstaluje niezbędne biblioteki oraz uruchomi skrypt.

### Krok 3: Ustawienie danych logowania
W pliku `kodzik.py` musisz ustawić swoje dane logowania do TikTok:
```python
username = 'TIKTOK_USERNAME'
password = 'TIKTOK_PASSWORD'