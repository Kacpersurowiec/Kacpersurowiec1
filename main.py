import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt



df = pd.read_csv('insurance.csv')
df_numeric = pd.get_dummies(df,drop_first=True)



korelacje = df_numeric.corr()['charges'].sort_values(ascending=False)

X = df_numeric.drop(columns='charges')
y = df_numeric['charges']

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)



model = RandomForestRegressor(random_state=42)
model.fit(train_X, train_y)

model.predict(test_X)


mae = mean_absolute_error(test_y, model.predict(test_X))
r2 = r2_score(test_y, model.predict(test_X))
print(mae)
print(r2)

waznosc_cech = model.feature_importances_

tabela_waznosci = pd.DataFrame({'Cecha' : train_X.columns,
                                'Waznosc' : waznosc_cech})

tabela_waznosci = tabela_waznosci.sort_values(by='Waznosc', ascending=True)

plt.figure(figsize=(15, 4))
plt.barh(tabela_waznosci['Cecha'], tabela_waznosci['Waznosc'], color='teal')
plt.xlabel('Wpływ na model (0.0 - 1.0)')
plt.title('Które cechy najbardziej wpływają na koszty medyczne?')
plt.show()


import pandas as pd

print("🏥 --- SYMULATOR KOSZTÓW MEDYCZNYCH --- 🏥")
print("Wpisz dane pacjenta, aby otrzymać wycenę.")

# 1. Zbieramy dane z klawiatury
wiek = int(input("Wiek (np. 30): "))
plec = input("Płeć (male/female): ")
bmi = float(input("BMI (np. 25.5): "))
dzieci = int(input("Liczba dzieci (np. 0): "))
palacz = input("Czy pali? (yes/no): ")
region = input("Region (southwest/southeast/northwest/northeast): ")

# 2. Tworzymy tabelę z jednym wierszem
nowy_pacjent = pd.DataFrame({
    'age': [wiek],
    'sex': [plec],
    'bmi': [bmi],
    'children': [dzieci],
    'smoker': [palacz],
    'region': [region]
})

# 3. Przetwarzamy tekst na liczby
nowy_pacjent_numeric = pd.get_dummies(nowy_pacjent)

# 4. KLUCZOWY KROK: Wyrównujemy kolumny do tych, które zna model (X_train)
nowy_pacjent_numeric = nowy_pacjent_numeric.reindex(columns=train_X.columns, fill_value=0)

# 5. Wyrok sztucznej inteligencji!
przewidywany_koszt = model.predict(nowy_pacjent_numeric)

print("\n=========================================")
print(f"💰 Przewidywany roczny koszt leczenia:")
print(f"💰 {przewidywany_koszt[0]:.2f} USD")
print("=========================================")