"""

1.	Készítsen programot a következő feladatok megoldására, melynek kódját nagykonyv.py néven mentse el. Olvassa be az UTF-8 kódolású konyvek.txt állományban lévő adatokat és tárolja el egy saját osztály (konyv) típusú listában! Ügyeljen rá, hogy az állomány első sora az adatok fejlécét tartalmazza! Az élő íróknak nincs megadva halálozási év. Az adatok tárolásakor ezeknél az íróknál a 2005-ös évet tárolja el halálozási évként!
2.	Hány könyv adatai szerepelnek az állományban?
3.	Írja ki a legjobb helyezést elért magyar könyv adatait a minta szerint!
4.	Bekerült-e a listába német nemzetiségű író könyve?
5.	Listázza ki az 90 évesnél idősebb írókat. A kortárs íróknál (akiknél nem szerepel halálozási év) a 2005-ös évet használja az életkor számításához! Ügyeljen arra, hogy a kiírásnál minden író csak egyszer szerepeljen! Az írók nevének sorrendje tetszőleges lehet.

"""
konyvek = []
with open('./Forrasok/02_feladat/konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
        next(forrasfajl)
        for sor in forrasfajl:
            adatok = sor.strip().split(';')
            nev = adatok[0]
            szul_ev = int(adatok[1])
            hal_ev = int(adatok[2])    if adatok[2] != ""  else 2005
            nemzetiseg = adatok[3]
            cim = adatok[4]
            helyezes = int(adatok[5])
            konyv = {'nev': nev, 'szul_ev': szul_ev, 'hal_ev': hal_ev, 'nemzetiseg' : nemzetiseg, 'cim' : cim, 'helyezes' : helyezes}
            konyvek.append(konyv)

print(f'{konyvek=}')
#3.2
print(f'3.2 Az állományban ennyi könyv adata szerepel: {len(konyvek)} db')

#3.3 feladat  
magyar_konyvek = []
for konyv in konyvek:
    if konyv ["nemzetiseg"] == 'magyar':
            magyar_konyvek.append(konyv)


legjobb_konyv = magyar_konyvek[0]
for konyv in magyar_konyvek:
    if konyv ["helyezes"] < legjobb_konyv['helyezes']:
        legjobb_konyv = konyv      
print(f"3.3 A legjobb helyezést elért magyar könyv: {legjobb_konyv["nev"]:} {legjobb_konyv["cim"]}")

#3.4
van = False
for konyv in konyvek:
    if konyv['nemzetiseg']  == "német":
            van = True
            break
if van:
        print("3.4 A listában szerepel német  író könyve")
else:
        print("A listában nincs német író könyve")

#3.5
idosebb_mint_90 =  set ()
for konyv in konyvek:
    if ((konyv['hal_ev']- konyv['szul_ev']) > 90):
        idosebb_mint_90.add(konyv['nev'])

print(idosebb_mint_90)
print("3.5 feladat: 90 évesnél idősebb írók")
for iro in idosebb_mint_90:
    print("\t" + iro)