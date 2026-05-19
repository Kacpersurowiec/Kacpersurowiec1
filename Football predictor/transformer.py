

def run_pipeline():
    import json
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    import joblib

    pd.options.display.max_columns = None

    def load_data(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            json_d = json.load(file)
            return json_d

    data = load_data('data/raw/mecze_pl.json')

    mecze = data['matches']

    print(mecze[0].keys())

    parsed_data = []
    def parse_matches(matches_list):
        for match in mecze:
            if match['status'] == 'FINISHED':
                row = {
                           "Data":  match['utcDate'],
                     'Home_name' : match['homeTeam']['name'],
                     'Away_name' :  match['awayTeam']['name'] ,
                     'home_goals': match['score']['fullTime']['home'] ,
                     'away_goals': match['score']['fullTime']['away'] ,
                }
                parsed_data.append(row)
        df = pd.DataFrame(parsed_data)
        return df
    df = parse_matches(mecze)

    df.to_csv('data/processed/mecze_pl_czyste.csv', index=False)

    def determine_winner(row):
        if row['home_goals'] > row['away_goals']:
            return 'H'
        elif row['home_goals'] < row['away_goals']:
            return 'A'
        else:
            return 'D'

    df['Wynik'] = df.apply(determine_winner, axis=1)

    y = df['Wynik']
    X = df.drop(['Wynik','home_goals', 'away_goals', 'Data'], axis=1)
    X = pd.get_dummies(X, columns=['Home_name', 'Away_name'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators= 1000,random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f' Skuteczność modelu: {accuracy * 100:.2f}%')

    joblib.dump(model, 'data/model_las_losowy.joblib')
    joblib.dump(list(X.columns), 'data/kolumny_treningowe.joblib')
