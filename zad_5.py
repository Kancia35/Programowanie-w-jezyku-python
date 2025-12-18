def type_hinting(numbers: list, pattern: int) -> bool:
    return pattern in numbers

if __name__ == "__main__":
    my_numbers = [10, 20, 30, 40, 50]
    print (type_hinting(my_numbers, 35))
