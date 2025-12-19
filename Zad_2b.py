def multiple_v1(number:list) -> list:
    extralist = []
    for x  in number:
        newnumber=x*2
        extralist.append(newnumber)
    return extralist


def multiple_v2(number:list) -> list:
    return [x * 2 for x in number]




if __name__ == '__main__':
#version 1
    example_v1 = [2, 4, 6, 8, 9]
    print(multiple_v1(example_v1))
#version 2
    example_v2 = [2, 4, 6, 8, 10]
    print(multiple_v2(example_v2))
