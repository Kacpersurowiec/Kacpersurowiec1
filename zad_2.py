
def pomnoz_liczby(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik


liczby = [1, 2, 3, 4, 5]

print(pomnoz_liczby(liczby))
