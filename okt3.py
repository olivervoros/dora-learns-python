# ============================================================
# PYTHON ALAPOK – GYAKORLÓ FELADATOK
# ------------------------------------------------------------
# DIÁK VÁLTOZAT  |  kb. 120 perc  |  27 feladat
# ============================================================
#
#   1. rész   Változók                          15 perc   (1–3.)
#   2. rész   Típusok és típuskonverzió         15 perc   (4–6.)
#   3. rész   f-string                          10 perc   (7–9.)
#   4. rész   input() - adatbekérés             10 perc   (10–12.)
#   5. rész   Listák                            20 perc   (13–16.)
#   6. rész   Ciklusok (for, while)             20 perc   (17–20.)
#   7. rész   if / elif / else                  15 perc   (21–23.)
#   8. rész   Hibakezelés (try / except)        15 perc   (24–26.)
#   Záró feladat, minden együtt                           (27.)
#
# HASZNÁLAT: olvasd el az EMLÉKEZTETŐT, futtasd a fájlt, nézd meg
# a demó kimenetét, aztán írd meg a feladatot a TODO alá.
# Minden feladatnál ott van, mit kell látnod, ha jól dolgoztál.


# ============================================================
# 1. RÉSZ – VÁLTOZÓK   (15 perc)
# ============================================================
#
# EMLÉKEZTETŐ
# -----------
# A változó egy DOBOZ, amire címkét ragasztasz. A címke a név,
# a doboz tartalma az érték.
#
#     nev = "Anna"
#     ^^^   ^^^^^^
#     címke  tartalom
#
# Az = jel NEM azt jelenti, hogy "egyenlő". Azt jelenti:
# "tedd bele a jobb oldalt a bal oldali dobozba".
# Ha új értéket teszel bele, a régi eltűnik.

print("=" * 60)
print("1. Változók")
print("=" * 60)

nev = "Anna"
kor = 16
print(nev)                    # Anna
print(kor)                    # 16

kor = 17                      # új érték, a 16 eltűnt
print(kor)                    # 17

kor = kor + 1                 # előbb kiszámolja a jobb oldalt, aztán beleteszi
print(kor)                    # 18

# ⚠️ A változónév nem kezdődhet számmal, és nem lehet benne
#    szóköz. Jó: elso_nev   Rossz: 1nev, elso nev
#
# ⚠️ A kis- és nagybetű számít: a Kor és a kor két külön doboz.
#
# 💡 Adj beszédes nevet: az "eletkor" többet mond, mint az "x".


# ------------------------------------------------------------
# 1. feladat ⭐
# ------------------------------------------------------------
# Hozz létre három változót: a kedvenc ételed neve, az ára
# forintban, és hogy hányszor etted a héten. Írd ki mindhármat.

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 2. feladat ⭐
# ------------------------------------------------------------
# Az alábbi pontszámhoz adj hozzá 10-et, aztán szorozd meg
# 2-vel, és írd ki. Mindig ugyanazt a változót használd!
# Elvárt kimenet: 70

pontszam = 25

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 3. feladat ⭐⭐
# ------------------------------------------------------------
# a) NE futtasd! Előbb írd le kommentbe, szerinted mit ír ki:
#
#        a = 5
#        b = a
#        a = 10
#        print(b)
#
# b) Cseréld meg a két pohár tartalmát úgy, hogy a végén
#    bal_pohar értéke "tej", jobb_pohar értéke "víz" legyen.
#    Elvárt kimenet: tej víz

bal_pohar = "víz"
jobb_pohar = "tej"

# TODO: ide írd a megoldást

# print(bal_pohar, jobb_pohar)


# ============================================================
# 2. RÉSZ – TÍPUSOK ÉS TÍPUSKONVERZIÓ   (15 perc)
# ============================================================
#
# EMLÉKEZTETŐ
# -----------
# Az "5" és az 5 a képernyőn ugyanúgy néz ki, de nem ugyanaz.
#
#     "5"   egy papírlap, amire az van írva, hogy öt
#      5    öt darab igazi pénzérme
#
# Két papírlapot egymás mellé tehetsz ("5" + "3" = "53"), de
# összeadni csak az érméket lehet (5 + 3 = 8).
#
# A négy alaptípus:
#     str     szöveg          "alma"
#     int     egész szám      42
#     float   tört szám       3.14
#     bool    igaz / hamis    True, False
#
# Átváltás (konverzió): int(), float(), str()

print()
print("=" * 60)
print("2. Típusok és típuskonverzió")
print("=" * 60)

print(type("alma"))           # <class 'str'>
print(type(42))               # <class 'int'>
print(type(3.14))             # <class 'float'>
print(type(True))             # <class 'bool'>

print("5" + "3")              # 53     összeragasztja
print(int("5") + int("3"))    # 8      összeadja
print("5" * 3)                # 555    háromszor egymás után
print(str(5) + " alma")       # 5 alma

# ⚠️ A tizedesjel PONT, nem vessző: 3.14
#
# ⚠️ Az int() levágja a törtrészt, nem kerekít: int(3.9) -> 3
#    Kerekíteni a round() tud: round(3.9) -> 4
#
# 💡 Ha nem tudod, mi van egy változóban: print(type(valtozo))


# ------------------------------------------------------------
# 4. feladat ⭐
# ------------------------------------------------------------
# Írd ki mind a négy változó típusát a type() segítségével.
# Előtte tippelj: melyik fog meglepni?

a = "2024"
b = 2024
c = 20.0
d = "True"

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 5. feladat ⭐
# ------------------------------------------------------------
# A két szám szövegként érkezett. Add össze őket úgy, hogy
# az eredmény 20 legyen, ne 128.

elso = "12"
masodik = "8"

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 6. feladat ⭐⭐
# ------------------------------------------------------------
# a) Számold ki és írd ki a fizetendő összeget (ár * darab).
#    Elvárt kimenet: 4500
# b) Alakítsd a "3.7" szöveget EGÉSZ számmá, és írd ki.
#    Elvárt kimenet: 3
#    Az int("3.7") hibát dob. Találd ki, hogyan lehet két
#    lépésben megcsinálni.

ar = "1500"
darab = 3
tort_szoveg = "3.7"

# TODO: ide írd a megoldást


# ============================================================
# 3. RÉSZ – f-STRING   (10 perc)
# ============================================================
#
# EMLÉKEZTETŐ
# -----------
# Az f-string olyan, mint egy előre megírt képeslap, amin
# üres helyek vannak: "Kedves ______, boldog ______. szülinapot!"
# A kapcsos zárójel az üres hely, a Python tölti ki.
#
#     f"Kedves {nev}, boldog {kor}. szülinapot!"
#     ^
#     az f betű nélkül nem működik!

print()
print("=" * 60)
print("3. f-string")
print("=" * 60)

nev = "Bence"
kor = 15
print(f"Kedves {nev}, boldog {kor}. szülinapot!")
print(f"Jövőre {kor + 1} éves leszel.")          # számolni is lehet benne

ar = 1299.5
print(f"Az ár: {ar:.2f} Ft")                     # 2 tizedesjegy: 1299.50
print(f"Az ár: {ar:.0f} Ft")                     # 0 tizedesjegy: 1300

# ⚠️ Ha lemarad az f, a kapcsos zárójel szó szerint kiíródik:
#    "Szia {nev}"  ->  Szia {nev}
#
# 💡 Az f-stringben nem kell str()-rel átváltani a számokat.


# ------------------------------------------------------------
# 7. feladat ⭐
# ------------------------------------------------------------
# Írd ki f-stringgel ezt a mondatot a változók segítségével:
# Luca Szegeden lakik és 14 éves.

tanulo = "Luca"
varos = "Szeged"
eletkor = 14

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 8. feladat ⭐⭐
# ------------------------------------------------------------
# Írd ki az árat pontosan két tizedesjeggyel.
# Elvárt kimenet: A termék ára: 1234.50 Ft

termek_ar = 1234.5

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 9. feladat ⭐⭐
# ------------------------------------------------------------
# Számold ki a területet a kapcsos zárójelen BELÜL (ne hozz
# létre új változót).
# Elvárt kimenet: A szoba 4 m x 2.5 m, a területe 10.0 m2.

szelesseg = 4
hosszusag = 2.5

# TODO: ide írd a megoldást


# ============================================================
# 4. RÉSZ – input() - ADATBEKÉRÉS   (10 perc)
# ============================================================
#
# EMLÉKEZTETŐ
# -----------
# Az input() egy POSTALÁDA. Bármit dobnak bele, az levélként,
# vagyis SZÖVEGKÉNT érkezik meg. Akkor is, ha számot írtak rá.
#
#     kor = input("Hány éves vagy? ")       # "16"  <- szöveg!
#     kor = int(input("Hány éves vagy? "))  #  16   <- szám
#
# Ebben a fájlban az input() sorok ki vannak kommentelve, és
# alattuk egy beégetett érték áll, hogy a fájl megállás nélkül
# lefusson. Ha ki akarod próbálni élőben: vedd ki a # jelet az
# input() elől, és tedd a beégetett sor elé.

print()
print("=" * 60)
print("4. input()")
print("=" * 60)

# nev = input("Mi a neved? ")
nev = "Dóri"
print(f"Szia, {nev}!")

# kor = int(input("Hány éves vagy? "))
kor = int("16")               # az input() ugyanígy szöveget adna
print(f"Jövőre {kor + 1} éves leszel.")

# ⚠️ Ha lemarad az int(), a kor + 1 hibát dob (TypeError),
#    mert szöveghez nem lehet számot adni.
#
# 💡 Tört számhoz float() kell: float(input("Magasság? "))


# ------------------------------------------------------------
# 10. feladat ⭐
# ------------------------------------------------------------
# Kérd be a felhasználó kedvenc színét, és írd ki:
# A kedvenc színed: kék

# szin = input("Mi a kedvenc színed? ")
szin = "kék"

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 11. feladat ⭐⭐
# ------------------------------------------------------------
# Kérd be a születési évet, és írd ki, hány éves lesz az
# illető 2030-ban. Alakítsd számmá az értéket!
# Elvárt kimenet: 2030-ban 20 éves leszel.

# szuletesi_ev = input("Melyik évben születtél? ")
szuletesi_ev = "2010"

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 12. feladat ⭐⭐
# ------------------------------------------------------------
# Kérj be egy távolságot kilométerben, váltsd át mérföldre
# (1 km = 0.621371 mérföld), és írd ki két tizedesjeggyel.
# Elvárt kimenet: 10.0 km = 6.21 mérföld

# km = input("Hány kilométer? ")
km = "10"

# TODO: ide írd a megoldást


# ============================================================
# 5. RÉSZ – LISTÁK   (20 perc)
# ============================================================
#
# EMLÉKEZTETŐ
# -----------
# A lista egy VONAT. A vagonok sorban állnak, mindegyikben
# van valami, és mindegyiknek van sorszáma.
#
# A sorszámozás 0-ról indul! Az első vagon a 0-s.
#
#     gyumolcsok = ["alma", "körte", "szilva"]
#                     0        1         2
#                    -3       -2        -1     (hátulról számolva)
#
# Szeletelés: lista[ettől:eddig]  - az "eddig" már NINCS benne.

print()
print("=" * 60)
print("5. Listák")
print("=" * 60)

gyumolcsok = ["alma", "körte", "szilva"]
print(gyumolcsok[0])          # alma      az első
print(gyumolcsok[-1])         # szilva    az utolsó
print(len(gyumolcsok))        # 3         hány elem van

gyumolcsok.append("barack")   # a végére
gyumolcsok.insert(0, "eper")  # az elejére (0. helyre)
gyumolcsok.remove("körte")    # érték szerint töröl
print(gyumolcsok)             # ['eper', 'alma', 'szilva', 'barack']

print(gyumolcsok[:2])         # ['eper', 'alma']    az első kettő
print(gyumolcsok[-2:])        # ['szilva', 'barack'] az utolsó kettő

szamok = [3, 1, 2]
print(sorted(szamok))         # [1, 2, 3]   ÚJ listát ad
print(szamok)                 # [3, 1, 2]   az eredeti nem változott
print(sum(szamok), max(szamok), min(szamok))     # 6 3 1

# ⚠️ lista[3] egy háromelemű listánál IndexError, mert a
#    sorszámok 0, 1, 2.
#
# ⚠️ A lista.sort() helyben rendez és None-t ad vissza.
#    SOHA ne írd: szamok = szamok.sort()  -> a listád eltűnik.
#
# 💡 "benne van-e?":  "alma" in gyumolcsok  ->  True


# ------------------------------------------------------------
# 13. feladat ⭐
# ------------------------------------------------------------
# Írd ki: az első napot, az utolsó napot (negatív indexszel),
# és hogy hány nap van a listában.
# Elvárt kimenet:
# hétfő
# péntek
# 5

napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek"]

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 14. feladat ⭐⭐
# ------------------------------------------------------------
# a) add a lista végére: "sajt"
# b) szúrd be a lista elejére: "kávé"
# c) töröld a "kenyér"-t
# d) írd ki a listát
# Elvárt kimenet: ['kávé', 'tej', 'tojás', 'sajt']

bevasarlas = ["tej", "kenyér", "tojás"]

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 15. feladat ⭐⭐
# ------------------------------------------------------------
# a) írd ki az első három elemet        -> [40, 10, 30]
# b) írd ki az utolsó két elemet        -> [20, 50]
# c) írd ki a listát növekvő sorrendben úgy, hogy az eredeti
#    NE változzon                       -> [10, 20, 30, 40, 50]
# d) írd ki az eredeti listát           -> [40, 10, 30, 20, 50]

ertekek = [40, 10, 30, 20, 50]

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 16. feladat ⭐⭐
# ------------------------------------------------------------
# Írd ki a jegyek összegét, a legjobb és a legrosszabb jegyet,
# és az átlagot (összeg osztva a darabszámmal).
# Elvárt kimenet:
# 19
# 5
# 2
# 3.8

jegyek = [5, 3, 4, 5, 2]

# TODO: ide írd a megoldást


# ============================================================
# 6. RÉSZ – CIKLUSOK (for, while)   (20 perc)
# ============================================================
#
# EMLÉKEZTETŐ
# -----------
# FOR ciklus: a tanár kioszt egy-egy füzetet MINDEN diáknak.
# Előre tudja, hányan vannak, sorban végigmegy rajtuk.
#
#     for diak in nevsor:
#         adj neki füzetet
#
# WHILE ciklus: addig kevered a levest, AMÍG fel nem forr.
# Nem tudod előre, hányszor kell, csak a feltételt figyeled.
#
#     while nem forr:
#         keverd meg
#
# range(1, 6) -> 1 2 3 4 5     az utolsó szám NINCS benne!

print()
print("=" * 60)
print("6. Ciklusok")
print("=" * 60)

for szam in range(1, 4):
    print(szam)                           # 1, 2, 3

for nev in ["Anna", "Béla"]:
    print(f"Szia, {nev}!")

osszeg = 0                                # üres vödör
for szam in range(1, 6):
    osszeg = osszeg + szam                # minden körben beleöntünk
print(osszeg)                             # 15

for sorszam, nev in enumerate(["Anna", "Béla"], start=1):
    print(f"{sorszam}. {nev}")            # 1. Anna / 2. Béla

visszaszamlalo = 3
while visszaszamlalo > 0:
    print(visszaszamlalo)                 # 3, 2, 1
    visszaszamlalo = visszaszamlalo - 1   # e nélkül soha nem áll meg!
print("Start!")

# ⚠️ A ciklus belsejét BEHÚZÁSSAL (4 szóköz) jelölöd. Ami nincs
#    behúzva, az már a ciklus után fut le, csak egyszer.
#
# ⚠️ Ha a while-ban semmi nem változtatja a feltételt, végtelen
#    ciklus lesz. Leállítás: Ctrl + C
#
# 💡 A "vödröt" (osszeg = 0) a ciklus ELŐTT hozd létre. Ha
#    belül van, minden körben kiürül.


# ------------------------------------------------------------
# 17. feladat ⭐
# ------------------------------------------------------------
# Írd ki a számokat 1-től 10-ig, mindet külön sorba.

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 18. feladat ⭐⭐
# ------------------------------------------------------------
# Add össze a számokat 1-től 100-ig for ciklussal, és írd ki
# az eredményt. Elvárt kimenet: 5050

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 19. feladat ⭐⭐
# ------------------------------------------------------------
# Írd ki a csapattagokat sorszámozva. Ne használj saját
# számláló változót, használd az enumerate-et!
# Elvárt kimenet:
# 1. Gergő
# 2. Hanna
# 3. Ákos

csapat = ["Gergő", "Hanna", "Ákos"]

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 20. feladat ⭐⭐
# ------------------------------------------------------------
# Egy baktérium minden órában megduplázódik. 1 darabbal
# indulunk. Hány óra múlva lesz belőle több, mint 1000?
# Használj while ciklust, és számold a köröket.
# Elvárt kimenet: 10 óra múlva 1024 baktérium van.

bakterium = 1
orak = 0

# TODO: ide írd a megoldást


# ============================================================
# 7. RÉSZ – if / elif / else   (15 perc)
# ============================================================
#
# EMLÉKEZTETŐ
# -----------
# Képzelj el egy FOLYOSÓT ajtókkal. Végigmész rajta, és az
# ELSŐ ajtón, ami kinyílik, bemész. A többit már meg sem nézed.
#
#     if    ->  az első ajtó
#     elif  ->  a következő ajtók (lehet több is)
#     else  ->  a folyosó vége, ha egyik ajtó sem nyílt ki
#
# Összehasonlítás:  ==  !=  <  >  <=  >=
# Összekötés:       and (mindkettő igaz)   or (legalább az egyik)

print()
print("=" * 60)
print("7. if / elif / else")
print("=" * 60)

homerseklet = 22

if homerseklet >= 30:
    print("Kánikula")
elif homerseklet >= 20:
    print("Kellemes idő")                 # ez fut le
elif homerseklet >= 10:
    print("Hűvös")
else:
    print("Hideg")

esik = False
if homerseklet >= 20 and not esik:
    print("Mehetünk a strandra")

# ⚠️ Egy = jel: értékadás.  Két == jel: összehasonlítás.
#    if kor = 18:   -> hiba!       if kor == 18:   -> jó
#
# ⚠️ A sorrend számít! A legszigorúbb feltétel legyen elöl.
#    Ha a ">= 10" lenne az első, a 22 fok is "Hűvös" lenne.
#
# 💡 Páros-e egy szám?  szam % 2 == 0   (a % a maradék)


# ------------------------------------------------------------
# 21. feladat ⭐
# ------------------------------------------------------------
# Írd ki, hogy a szám "páros" vagy "páratlan".
# Elvárt kimenet: páratlan

szam = 7

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 22. feladat ⭐⭐
# ------------------------------------------------------------
# Írd meg az osztalyzat(pont) függvényt, ami visszaadja a jegyet:
#     90 vagy több   -> 5
#     75 – 89        -> 4
#     60 – 74        -> 3
#     40 – 59        -> 2
#     40 alatt       -> 1

def osztalyzat(pont):
    # TODO: ide írd a megoldást
    pass


# Teszt:
# print(osztalyzat(95))       # 5
# print(osztalyzat(75))       # 4
# print(osztalyzat(59))       # 2
# print(osztalyzat(40))       # 2
# print(osztalyzat(10))       # 1


# ------------------------------------------------------------
# 23. feladat ⭐⭐
# ------------------------------------------------------------
# Írd meg a belepo(kor, diak) függvényt. A diak True vagy False.
#     6 év alatt                     -> 0 Ft
#     diák VAGY 65 éves és afölött   -> 1000 Ft
#     mindenki más                   -> 2000 Ft

def belepo(kor, diak):
    # TODO: ide írd a megoldást
    pass


# Teszt:
# print(belepo(4, False))     # 0
# print(belepo(20, True))     # 1000
# print(belepo(30, False))    # 2000
# print(belepo(70, False))    # 1000


# ============================================================
# 8. RÉSZ – HIBAKEZELÉS (try / except)   (15 perc)
# ============================================================
#
# EMLÉKEZTETŐ
# -----------
# A try/except a VÉDŐHÁLÓ a cirkuszi artista alatt. Nem
# akadályozza meg, hogy leessen, de ha leesik, nem ér véget
# az előadás.
#
#     try:
#         kockázatos művelet
#     except HibaNeve:
#         mit csináljunk, ha baj van
#
# A leggyakoribb hibák:
#     ValueError          int("alma")       jó típus, rossz tartalom
#     TypeError           "5" + 5           rossz típus
#     ZeroDivisionError   10 / 0            nullával osztás
#     IndexError          [1, 2][5]         nincs ilyen sorszám

print()
print("=" * 60)
print("8. Hibakezelés")
print("=" * 60)

szoveg = "tizenkettő"

try:
    szam = int(szoveg)
    print(szam * 2)
except ValueError:
    print("Ez nem szám!")                 # ez fut le

print("A program megy tovább.")

# ⚠️ Mindig írd oda a hiba NEVÉT. A sima "except:" mindent
#    elkap, a saját elgépelésedet is, és nem látod, mi a baj.
#
# 💡 A hiba nevét a piros hibaüzenet utolsó sorának elején
#    találod. Okozz hibát szándékosan, és olvasd el!


# ------------------------------------------------------------
# 24. feladat ⭐
# ------------------------------------------------------------
# Próbáld számmá alakítani a szöveget. Ha nem sikerül, írd ki:
# Ez nem szám!

bemenet = "alma"

# TODO: ide írd a megoldást


# ------------------------------------------------------------
# 25. feladat ⭐⭐
# ------------------------------------------------------------
# Írd meg a biztonsagos_osztas(a, b) függvényt. Adja vissza
# a / b értékét, de ha b nulla, akkor írja ki, hogy
# "Nullával nem lehet osztani!", és adjon vissza None-t.

def biztonsagos_osztas(a, b):
    # TODO: ide írd a megoldást
    pass


# Teszt:
# print(biztonsagos_osztas(10, 2))    # 5.0
# print(biztonsagos_osztas(10, 0))    # Nullával nem lehet osztani!  majd  None


# ------------------------------------------------------------
# 26. feladat ⭐⭐
# ------------------------------------------------------------
# Írd ki a lista "hanyadik" sorszámú elemét. Ha nincs ilyen,
# írd ki: Nincs ilyen elem!
# Előbb derítsd ki, mi a hiba pontos neve.

szinek = ["piros", "zöld", "kék"]
hanyadik = 5

# TODO: ide írd a megoldást


# ============================================================
# ZÁRÓ FELADAT – minden együtt
# ============================================================

# ------------------------------------------------------------
# 27. feladat ⭐⭐⭐
# ------------------------------------------------------------
# Egy bolti kassza beolvasta a tételek árait, de néhány hibás.
#
#   - menj végig a listán for ciklussal
#   - alakítsd számmá az árakat
#   - a hibásakat hagyd ki, de írd ki, melyik volt az
#   - a jó árakat gyűjtsd egy új listába
#   - számold meg a hibásakat
#   - a végén írd ki a részösszeget
#   - ha a részösszeg 2000 Ft fölött van, jár 10% kedvezmény
#   - írd ki a kedvezményt és a fizetendő összeget
#
# Elvárt kimenet:
# Kihagyva: 'ingyen'
# Kihagyva: ''
# 4 jó tétel, 2 hibás
# Részösszeg: 2650 Ft
# Kedvezmény: 265 Ft
# Fizetendő: 2385 Ft

tetelek = ["450", "700", "ingyen", "1200", "", "300"]

# TODO: ide írd a megoldást


# ============================================================
# AMIT MA GYAKOROLTUNK
# ============================================================
#
#   Változó        doboz címkével. Az = beletesz, nem összehasonlít.
#   Típusok        str, int, float, bool. Az "5" nem 5.
#   Konverzió      int(), float(), str()
#   f-string       f"Szia {nev}"  és  {ar:.2f}
#   input()        MINDIG szöveget ad, számhoz int() vagy float() kell
#   Lista          0-tól számoz, [-1] az utolsó, [ettől:eddig]
#   for            minden elemre egyszer
#   while          amíg a feltétel igaz
#   if/elif/else   az első igaz ág fut le, a sorrend számít
#   try/except     védőháló, mindig a hiba nevével
#
# HA CSAK HÁROM DOLGOT JEGYZEL MEG:
#   1. Az input() szöveget ad. Alakítsd át rögtön.
#   2. A lista és a range is 0-tól számol, és a vége nincs benne.
#   3. Olvasd el a hibaüzenet utolsó sorát. Ott a megoldás fele.