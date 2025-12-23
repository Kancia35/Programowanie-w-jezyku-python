def even_number(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    check = even_number(10)
    if check is True:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
