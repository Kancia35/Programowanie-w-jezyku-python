def even_numbers(number: list) -> list:
    result = []
    for x in range(len(number)):
        if x % 2 == 0:
            result.append(x)
    return result


if __name__ == '__main__':
    print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))