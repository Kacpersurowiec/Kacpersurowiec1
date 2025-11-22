def czy_parzysta(a :int) -> bool:
    return a % 2 == 0

wynik = czy_parzysta(6)

if wynik is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

