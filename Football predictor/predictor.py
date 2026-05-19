import json
import pandas as pd
import joblib

model = joblib.load('data/model_las_losowy.joblib')
treningowe_kolumny = joblib.load('data/kolumny_treningowe.joblib')


with open('data/raw/mecze_pl.json', 'r', encoding='utf-8') as f:
    dane = json.load(f)


przyszle_mecze = []
for match in dane['matches']:
    if match['status'] == 'SCHEDULED':
        przyszle_mecze.append({
            'Data': match['utcDate'],
            'Home_name': match['homeTeam']['name'],
            'Away_name': match['awayTeam']['name']
        })


df_przyszlosc = pd.DataFrame(przyszle_mecze)


if df_przyszlosc.empty:
    print("\n" + "=" * 50)
    print(" Nie ma zaplanowanych meczów")
    print("=" * 50)
    print("Zbiór 'SCHEDULED' jest pusty.")
else:

    df_przyszlosc = df_przyszlosc.head(10)

    X_przyszlosc = df_przyszlosc.drop(columns=['Data'])
    X_przyszlosc = pd.get_dummies(X_przyszlosc, columns=['Home_name', 'Away_name'])


    X_przyszlosc = X_przyszlosc.reindex(columns=treningowe_kolumny, fill_value=0)


    wyniki = model.predict(X_przyszlosc)


    print("\n" + "=" * 50)
    print("Typy:")
    print("=" * 50)

    for i in range(len(df_przyszlosc)):
        gospodarz = df_przyszlosc.iloc[i]['Home_name']
        gosc = df_przyszlosc.iloc[i]['Away_name']
        typ = wyniki[i]

        if typ == 'H':
            znaczek = "1 (Wygra Gospodarz)"
        elif typ == 'A':
            znaczek = "2 (Wygra Gość)"
        else:
            znaczek = "X (Remis)"

        print(f"{gospodarz.ljust(25)} vs {gosc.rjust(25)}  ==>  WYTYPOWANO: {znaczek}")