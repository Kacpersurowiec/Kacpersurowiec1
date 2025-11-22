
def dwie_listy(lista1 : list, lista2 : list) -> list:
    suma = lista1 + lista2
    bez_duplikatow = list(set(suma))
    potegi = [x ** 3 for x in bez_duplikatow]
    return potegi

listaA = [1, 2, 3]
listaB = [3, 4, 5]
wynik = dwie_listy(listaA, listaB)

print(wynik)