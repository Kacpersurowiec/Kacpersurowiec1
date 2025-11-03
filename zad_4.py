def parzyste_elementy(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)


liczby = list(range(11))

parzyste_elementy(liczby)
