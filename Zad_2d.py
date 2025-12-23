def even_numbers(number: list) -> list:
    result = []
    for x in range(len(number)):
        if x % 2 != 0:
            result.append(number[x])
    return result


if __name__ == '__main__':
    print(even_numbers([2, 3, 4, 6, 7, 8, 9, 33, 88, 90]))
