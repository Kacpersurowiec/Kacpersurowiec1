class Property:
    def __init__(self, area, rooms, price, address):
        self.area = int(area)
        self.rooms = int(rooms)
        self.price = int(price)
        self.address = str(address)

    def __str__(self):
        return (
            f"Adres: {self.address}, Powierzchnia: {self.area} m2, "
            f"Pokoje: {self.rooms}, Cena: {self.price} PLN"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = int(floor)

    def __str__(self):
        return (
            f"Adres: {self.address}, Powierzchnia: {self.area} m2, "
            f"Pokoje: {self.rooms}, Cena: {self.price} PLN, "
            f"Piętro: {self.floor}"
            )


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = int(plot)

    def __str__(self):
        # Zawijanie linii i poprawa spójności formatowania
        return (
            f"Adres: {self.address}, Powierzchnia: {self.area} m2, "
            f"Pokoje: {self.rooms}, Cena: {self.price} PLN, "
            f"Działka: {self.plot} m2"
        )
