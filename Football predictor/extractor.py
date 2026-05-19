import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    print("Nie znalazłem klucza API. Sprawdź plik .env")
else:
    print("klucz załadowany ")

def fetch_matches(API_KEY, competition_code):
    url = f'http://api.football-data.org/v4/competitions/{competition_code}/matches'
    headers = {"X-Auth-Token" : API_KEY}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200 :
            return response.json()
        else:
            print(f'Błąd api : {response.status_code}')
            return None

    except Exception as e:
        print(f'Błąd połączenia {e}')
        return None


def save_to_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

mecze_pl = fetch_matches(API_KEY, 'PL')

if mecze_pl:
    save_to_json(mecze_pl, f'data/raw/mecze_pl.json')
    print(mecze_pl)