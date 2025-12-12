def type_hinting(names: list, zawod: list) -> list:
    merged = list(set(names + zawod))
    result = [x**3 for x in merged]
    return result

l1 = [1, 2, 3]
l2 = [4, 5, 3]
print (type_hinting(l1, l2))
