def czy_zawiera(lista: list, wartosc: int) -> bool:
    return wartosc in lista


liczby = [1, 2, 3, 4]
przyklad = czy_zawiera(liczby, 3)

print(przyklad)
