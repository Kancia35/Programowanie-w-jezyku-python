class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Dom w {self.address}:\n"
                f"  Area: {self.area} m²\n"
                f"  Rooms: {self.rooms}\n"
                f"  Price: {self.price}\n"
                f"  Plot size: {self.plot} m²")


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie w {self.address}:\n"
                f"  Area: {self.area} m²\n"
                f"  Rooms: {self.rooms}\n"
                f"  Price: {self.price}\n"
                f"  Floor: {self.floor}")


house = House(area=120, rooms=5, price=900000, address="Gliwice, ul. Chorzowska 19", plot=600)
flat = Flat(area=84, rooms=2, price=450000, address="Gliwice, ul. Daszyńskiego 17", floor=4)


print(house)
print(flat)
