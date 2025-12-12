def type_hinting(number: int) -> bool:
    return number % 2 == 0
if (type_hinting(10))==True: print("liczba parzysta")
else: print("liczba nieparzysta")