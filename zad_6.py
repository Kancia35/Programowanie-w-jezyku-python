def merged_lists(list1: list, list2: list) -> list:
    merged = list(set(list1 + list2))
    result = [x**3 for x in merged]
    return result


if __name__ == "__main__":
    l1 = [1, 2, 3]
    l2 = [4, 5, 3]
    print(merged_lists(l1, l2))
