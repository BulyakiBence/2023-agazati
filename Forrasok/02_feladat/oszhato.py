"""
Írjon programot oszthato.py néven. A programban hozzon létre egy függvényt oszthato néven, ami egy egész számot kap paraméterként és igaz értéket ad vissza, ha a szám 7-tel osztható, de 3-mal nem. A függvény segítségével számolja ki azon 3 jegyű számok átlagát, amire a függvény igaz értékkel tér vissza.
Minta:
A 7-tel osztható és 3-mal nem osztható 3 jegyű számok átlaga: 551.2705882352941

"""
def oszthato(szam):
    if szam % 7 == 0 and szam % 3 != 0:
        return True
    else: 
        return False
    
#print(oszthato(7))
#print(oszthato(21))
#darab = 0
osszeg = 0
for i in range(100,1000):
    if oszthato(i):
        darab += 1
        osszeg += i
hettel_oszhato_de_3mal_nenm = osszeg / darab
print(f"A 7-tel osztható és 3-mal nem osztható 3 jegyű számok átlaga: {hettel_oszhato_de_3mal_nenm}")