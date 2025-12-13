class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Dom | {self.address}, {self.area} m2, pokoje: {self.rooms}, działka: {self.plot}, cena: {self.price}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Mieszkanie | {self.address}, {self.area} m2, pokoje: {self.rooms}, piętro: {self.floor}, cena: {self.price}"


house = House(120, 4, 800000, "Warszawa, ul. Leśna 5", 500)
flat = Flat(55, 2, 450000, "Kraków, ul. Krótka 3", 2)

print(house)
print(flat)