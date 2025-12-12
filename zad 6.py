def type_hinting(liczby: list, wzor: int) -> bool:
    return wzor in liczby

moje_liczby = [10, 20, 30, 40, 50]
print (type_hinting(moje_liczby, 35))