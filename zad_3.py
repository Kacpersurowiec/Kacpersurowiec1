
class Property:
    def __init__(self, area, rooms, price, adress):
        self.area = int(area)
        self.rooms = int(rooms)
        self.price = int(price)
        self.adress = str(adress)

    def __str__(self):
        return (
            f"Adres: {self.adress}  , Powierzchnia : {self.area},"
            f"Pokoje: {self.rooms}, Cena:      {self.price} PLN"
        )

class House(Property):
    def __init__(self, area, rooms, price, adress, plot):
        super().__init__(area,rooms,price,adress)
        self.plot = int(plot)

    def __str__(self):
        return (f'Adres: {self.adress},'
                f'Powierzchnia : {self.area},'
                f'Pokoje: {self.rooms}, Cena: {self.price} PLN'
                f'        Dzialka: {self.plot} m2'
                )

class Flat(Property):
    def __init__(self, area, rooms, price, adress, floor):
        super().__init__(area,rooms,price,adress)
        self.floor = int(floor)

    def __str__(self):
        return  (f'Adres: {self.adress},'
         f'     Powierzchnia : {self.area},'
         f'     Pokoje: {self.rooms}'
         f'     Cena: {self.price} PLN'
         f'     Pietro: {self.floor} ')

moj_dom = House( 150, 5, 1800000,'Czerwona 5', 300)

moje_mieszkanie = Flat(55, 3, 500000, 'Czerwona 10', 3)
print(moj_dom)
print(moje_mieszkanie)

