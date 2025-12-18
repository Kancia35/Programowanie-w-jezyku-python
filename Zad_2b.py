def mnozenie(liczba:list):
    pomnozone = []
    for x  in liczba:
        nowaliczba=x*2
        pomnozone.append(nowaliczba)
    return pomnozone

liczby = [2, 4, 6, 8, 9]
print(mnozenie(liczby))



def pomnoz_przez_dwa(liczba:list):
    return [x * 2 for x in lista]

liczby = [2, 4, 6, 8, 9]
wynik = pomnoz_przez_dwa(liczby)
print(wynik)
