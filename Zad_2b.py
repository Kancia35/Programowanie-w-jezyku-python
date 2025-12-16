def mnozenie(liczba:list):
    pomnozone = []
    for x  in liczba:
        nowaliczba=x*2
        pomnozone.append(nowaliczba)
    return pomnozone

liczby = [2, 4, 6, 8, 9]
print(mnozenie(liczby))


