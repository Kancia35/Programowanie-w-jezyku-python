def even_number(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    check = even_number(10)
    if check is True:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
