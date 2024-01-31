# WykopWTF

Wykop WTF - Wykrywacz Treści Frywolnych

Dokumentacja opisuje aplikacje, która scrapuje wpisy użytkowników z różnych stron internetowych, a następnie używa modelu do weryfikacji, czy wpis jest nacechowany pozytywnie czy negatywnie. Do zainstalowania aplikacji wymagany jest python >= 3.9.2

# Spis treści
1. Instalacja.  
2. Struktura projektu.  
3. Uruchamianie aplikacji.  
4. API endpoints.  
5. Testy.  
6. Sposób użytkowania.  

# 1. Instalacja

## 1.1. Pobieranie kodu źródłowego  
Zacznij od pobrania kodu źródłowego z repozytorium projektu. Możesz sklonować repozytorium za pomocą Git, wykonując poniższe polecenie w terminalu:
```
git clone https://github.com/JakubDz2208/WykopWTF.git
```
<br>

## 1.2. Tworzenie i aktywacja środowiska wirtualnego (opcjonalne, ale zalecane)
Stworzenie środowiska wirtualnego pozwoli na izolację zależności projektu od innych projektów w systemie. Wykonaj następujące polecenia:
```
python -m venv .venv
venv\Scripts\activate
```
<br>

## 1.3. Instalacja zależności
Zainstaluj niezbędne biblioteki Pythona, korzystając z pliku requirements.txt. Wykonaj poniższe polecenie:
```
pip install -r requirements.txt
```
<br>

# 2. Struktura projektu
- app
  - model
    - BAN-PL.csv
    - dataset.ipynb
    - modael.joblib
    - tfidf_vectorizer.joblib
  - scraper
    - sraper.py
  - tests
    - conftest.py
    - test_scraper.py
    - test_website.py
  - website
    - static
        - style.css
    - templates
        - template.html
- .gitignore
- pytest.ini
- README.md
- requirements.txt
    
<br>

# 3. Uruchamianie aplikacji
Aby uruchomić aplikację, użyj poniższego polecenia:
```
python website/web_app.py
```
<br>

# 4. API endpoints
Aplikacja udostępnia endpoint API do scrapowania i weryfikacji nacechowania komentarzy:

- POST /api/scrape_comments  
    - Wysyła zapytanie z parametrami url (adres strony do scrapowania) i opcjonalnym limit (limit ilości komentarzy do pobrania). Odpowiada danymi w formie JSON z predykcjami nacechowania komentarzy.

<br>

# 5. Testy
Testy aplikacji znajdują się w katalogu **tests/** Aby uruchomić testy, użyj poniższego polecenia:
```
pytest -v
```
<br>

Dodatkowo W procesie testowania użyto dwóch adnotacji **mark** z biblioteki **pytest**:

**@mark.scraper:** Oznacza testy, które są wykonywane tylko dla scrapera aplikacji. Aby uruchomić testy tylko dla tej części, nalezy użyć polecenia:
```
pytest -m scraper
```

**@mark.website:** Oznacza testy, które są wykonywane tylko dla strony internetowej aplikacji. Aby uruchomić testy tylko dla tej części, nalezy użyć polecenia:
```
pytest -m website
```
<br>

# 6. Sposób użytkowania 
### 6.1. Wpisz nazwę wątku:
Wypełnij pole "Wpisz nazwę wątku" nazwą wątku, którego wpisy chcesz przeszukać. Na przykład: "polityka".

### 6.2. Ustaw limit rekordów:
Określ limit rekordów, które chcesz pobrać. Domyślnie ustawiony na 5.

### 6.3. Lista wpisów:
Kliknij przycisk "Lista wpisów", aby rozpocząć proces przeszukiwania i analizy wpisów.


### 6.4. Przewijanie Stron:
Po przeszukaniu wpisów, możesz przewijać się między stronami, korzystając z przycisków "Poprzednia" i "Następna".

### 6.5. Tabela Wpisy:
Pod tabela znajdziesz listę wpisów w formie tabeli, obejmującej numer wpisu, treść wpisu i informację, czy jest on nacechowany negatywnie.

<br>

## Autorzy

Michał 46873  
Jakub 48022  
Jakub 46023  
Łukasz 46968  
Patryk 45042  
