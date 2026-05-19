from extractor import API_KEY, save_to_json, fetch_matches
from transformer import run_pipeline
import schedule
import time

def start():
    Dane_z_api = fetch_matches(API_KEY, 'PL')

    if Dane_z_api:
        save_to_json(Dane_z_api, 'data/raw/mecze_pl.json')

        run_pipeline()
        print('Udało się')
    else:
        print('Nie udało się pobrać danych z api')
if __name__ == '__main__':
    schedule.every().monday.at('10:00').do(start)
    while True:
        schedule.run_pending()
        time.sleep(1)


