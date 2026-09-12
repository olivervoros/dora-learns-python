"""
=========================================================================
PYTHON ALAPOK - TELJES LECKE  (diák példány)          kb. 120-150 perc
=========================================================================

  1. rész   Változók                          15 perc
  2. rész   Típusok és típuskonverzió         15 perc
  3. rész   f-string                          10 perc
  4. rész   input() - adatbekérés             10 perc
  5. rész   Listák                            20 perc
  6. rész   Ciklusok (for, while)             20 perc
  7. rész   if / elif / else                  15 perc
  8. rész   Hibakezelés (try / except)        15 perc
  9. rész   Fájlkezelés                       20 perc

  Utána:    20 feladat, a magyarázatok alatt, részenként.

HOGYAN HASZNÁLD
---------------
  Nyisd meg ezt a fájlt a szerkesztőd egyik oldalán, egy üres
  gyakorlas.py fájlt a másikon. Olvasd el az EMLÉKEZTETŐ blokkot,
  futtasd a mintakódot, majd ÍRD BE a saját megoldásodat a feladatra,
  mielőtt megnézed a tanári fájlt.

  A kód, amit legépelsz, megmarad. A kód, amit csak elolvasol, nem.

  Futtatás:   python 03_alapok_lecke_diak.py

MEGJEGYZÉS
  A fájlban nincs élő input() hívás, hogy végig lefusson megállás
  nélkül. Az élő verziók kommentben ott vannak mellettük.

  Minden példa Python 3.11-en le lett futtatva.
"""

import os


def cim(szoveg):
    print("\n" + "=" * 70)
    print(szoveg)
    print("=" * 70)


def alcim(szoveg):
    print("\n" + szoveg)
    print("-" * len(szoveg))


# =========================================================================
# 1. RÉSZ - VÁLTOZÓK
# =========================================================================

cim("1. RÉSZ - VÁLTOZÓK  (15 perc)")

print("""
EMLÉKEZTETŐ - a változó egy felcímkézett doboz
----------------------------------------------
  Képzelj el egy polcot tele dobozokkal. Minden dobozon van egy címke,
  és a dobozban van valami:

      nev = "Anna"          a "nev" címkéjű dobozba betettük: Anna
      eletkor = 34          az "eletkor" címkéjű dobozba betettük: 34

  Az = jel nem azt jelenti, hogy "egyenlő". Azt jelenti: "TEDD BELE".
  Balra a címke, jobbra amit beleteszünk.

  Ha újra ráírod a címkét, a régi tartalom kiesik:

      eletkor = 35          a 34 eltűnt, most 35 van a dobozban

  ⚠️  A név nem kezdődhet számmal, nem lehet benne szóköz, és a Python
      megkülönbözteti a kis- és nagybetűt: nev és Nev két külön doboz.

  💡  Adj beszédes nevet. A "x" doboz két hét múlva rejtvény lesz,
      a "tanulo_eletkora" nem.
""")

alcim("Nézd meg futás közben")
nev = "Anna"
eletkor = 34
magassag = 1.67

print("nev      =", nev)
print("eletkor  =", eletkor)
print("magassag =", magassag)

eletkor = eletkor + 1  # ugyanabba a dobozba, eggyel több
print("egy év múlva:", eletkor)

a, b = 1, 2  # két doboz egy sorban
a, b = b, a  # és a csere
print("csere után: a =", a, " b =", b)


# -------------------------------------------------------------------------
# FELADATOK - 1. rész
# -------------------------------------------------------------------------
"""
1. feladat  ⭐  Bemutatkozás
   Készíts három változót: nev (szöveg), eletkor (egész szám),
   magassag (tizedes szám). Írd ki mindhármat külön sorban.

2. feladat  ⭐  Csere
   Van két változód: elso = "tea", masodik = "kávé".
   Cseréld meg a tartalmukat, és írd ki őket a csere után.
   Egy sorban is meg tudod oldani.
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# 2. RÉSZ - TÍPUSOK ÉS TÍPUSKONVERZIÓ
# =========================================================================

cim("2. RÉSZ - TÍPUSOK ÉS TÍPUSKONVERZIÓ  (15 perc)")

print("""
EMLÉKEZTETŐ - kártya vagy érme?
-------------------------------
  Képzeld el, hogy van egy kártyád, amire rá van írva: "öt".
  És van öt darab érméd.

  A kettő ránézésre ugyanarról szól, de nem ugyanaz.
  Két kártyát egymás mellé téve ("öt" "három") egy hosszabb feliratot
  kapsz, nem nyolc érmét.

  Pontosan ez történik a Pythonban:

      "5" + "3"   ->  "53"     két kártya egymás mellett
       5  +  3    ->   8       két maréknyi érme összeöntve

  A NÉGY ALAPTÍPUS, amivel most dolgozunk:

      str     szöveg          "Anna", "5", "kávé"
      int     egész szám      34, 0, -7
      float   tizedes szám    1.67, 0.5, 3.0
      bool    igaz/hamis      True, False

  ÁTVÁLTÁS = a kártyából érme, vagy az éremből kártya:

      int("5")      ->  5        szövegből egész szám
      float("1.5")  ->  1.5      szövegből tizedes
      str(5)        ->  "5"      számból szöveg
      int(3.9)      ->  3        LEVÁGJA a tizedeseket, nem kerekít!

  ⚠️  int("alma") hibával leáll. Erről a 8. részben lesz szó.
  ⚠️  int(3.9) az 3, nem 4. Ha kerekíteni akarsz: round(3.9) -> 4.

  💡  type(valami) megmondja, milyen típusú. Ha valami furcsán
      viselkedik, ez az első kérdés, amit fel kell tenni.
""")

alcim("Nézd meg futás közben")
a = "5"
b = "3"
print('"5" + "3"        ->', a + b, "   <- összeragasztva")
print("int(a) + int(b)  ->", int(a) + int(b), "    <- összeadva")
print('"5" * 3          ->', a * 3, " <- háromszor egymás után")
print("int(a) * 3       ->", int(a) * 3, "   <- megszorozva")

print("type(a)          ->", type(a).__name__)
print("type(int(a))     ->", type(int(a)).__name__)

print("int(3.9)         ->", int(3.9), "    <- levágja")
print("round(3.9)       ->", round(3.9), "    <- kerekíti")
print("float('1.5')     ->", float("1.5"))
print("str(5) + ' db'   ->", str(5) + " db")


# -------------------------------------------------------------------------
# FELADATOK - 2. rész
# -------------------------------------------------------------------------
"""
3. feladat  ⭐  Mit ír ki?
   Írd le PAPÍRRA (vagy kommentbe), mit ír ki ez a hat sor, MIELŐTT
   lefuttatnád. Utána futtasd le és ellenőrizd:

       x = "7"
       print(x + x)
       print(int(x) + int(x))
       print(x * 2)
       print(int(x) * 2)
       print(type(x))
       print(type(float(x)))

4. feladat  ⭐  Átváltás
   Van egy szöveges változód: ar_szoveg = "1250".
   a) Alakítsd egész számmá, és add hozzá a 250-et.
   b) Alakítsd vissza szöveggé, és ragaszd mögé azt, hogy " Ft".

5. feladat  ⭐⭐  A klasszikus hiba
   Ez a sor hibával leáll:

       osszeg = "10" + 5

   Mondd el egy mondatban, miért, és írd le KÉT különböző javítást:
   egyet, ahol 15 lesz az eredmény, és egyet, ahol "105".
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# 3. RÉSZ - F-STRING
# =========================================================================

cim("3. RÉSZ - F-STRING  (10 perc)")

print("""
EMLÉKEZTETŐ - az űrlap a kihagyott helyekkel
--------------------------------------------
  Ismered azokat az űrlapokat, ahol a szöveg elő van nyomtatva, és
  csak a pontozott vonalakra kell beírni az adatokat?

      "Alulírott .............. , életkor ....... , kijelentem..."

  Az f-string pontosan ez. Előre megírod a mondatot, és ahol adat kell,
  kapcsos zárójelet teszel. A Python kitölti.

      print(f"{nev} {eletkor} éves.")

  Az f betű a nyitó idézőjel ELŐTT áll. Ha lemarad, a kapcsos zárójel
  szó szerint kiíródik.

  FORMÁZÁS - a kettőspont után jön a formátum:

      f"{ar:.2f}"      két tizedesjegy          ->  1250.00
      f"{nev:>10}"     jobbra igazítva 10 helyre
      f"{nev:<10}"     balra igazítva
      f"{szam:,}"      ezres tagolás            ->  1,250,000

  ⚠️  A kapcsos zárójelbe KIFEJEZÉS kerül, nem idézőjeles szöveg
      másolása: f"{eletkor + 1}" működik, és ez a lényege.

  💡  A régi módszerek (+ jel, .format(), %) még működnek, de ma
      f-stringet írunk. Rövidebb és jobban olvasható.
""")

alcim("Nézd meg futás közben")
nev = "Anna"
eletkor = 34
ar = 1250.5

print(f"{nev} {eletkor} éves.")
print(f"Jövőre {eletkor + 1} lesz.")
print(f"Az ár: {ar:.2f} Ft")
print(f"Az ár: {ar:.0f} Ft   <- nulla tizedes")
print(f"|{nev:<10}|{nev:>10}|   <- balra, majd jobbra igazítva")
print(f"Nagy szám: {1250000:,}".replace(",", " "))
print(f"Idézőjel nélkül is: {'kis' + 'kutya'}")


# -------------------------------------------------------------------------
# FELADATOK - 3. rész
# -------------------------------------------------------------------------
"""
6. feladat  ⭐  Egy mondat
   Az 1. feladat három változójával írj ki EGY mondatot f-stringgel:
       "Anna 34 éves és 1.67 m magas."

7. feladat  ⭐⭐  Számla
   Adott: termek = "kávé", darab = 3, egysegar = 690.
   Írj ki egy sort ilyen formában:
       "3 x kávé = 2070.00 Ft"
   A szorzást magában az f-stringben végezd el, két tizedesjeggyel.
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# 4. RÉSZ - INPUT() - ADATBEKÉRÉS
# =========================================================================

cim("4. RÉSZ - INPUT() - ADATBEKÉRÉS  (10 perc)")

print("""
EMLÉKEZTETŐ - a postaláda
-------------------------
  Az input() egy postaláda. Bárki bármit bedob rajta, az LEVÉLKÉNT
  érkezik meg - vagyis SZÖVEGKÉNT. Akkor is, ha számot írt.

      valasz = input("Hány éves vagy? ")
      print(valasz + 1)        ⚠️ HIBA! szöveghez nem adhatsz számot

  A megoldás: alakítsd át rögtön az ajtóban, ugyanabban a sorban.

      eletkor = int(input("Hány éves vagy? "))

  ⚠️  Ez a lecke leggyakoribb kezdő hibája. Ha valami "működnie
      kellene, de nem", nézd meg, nem maradt-e szöveg a számod.

  ⚠️  Ha a felhasználó "alma"-t ír a szám helyére, az int() elszáll.
      A 8. részben megtanuljuk elkapni.

  💡  A .strip() levágja a véletlen szóközöket a két végéről:
          nev = input("Neved: ").strip()
""")

alcim("Nézd meg futás közben (itt előre beírt értékekkel)")

# ÉLES VERZIÓ (órán ezt használd):
# km = float(input("Hány kilométer? "))

km = 10.0  # ide most beírjuk kézzel
mertfold = km * 0.621371
print(f"{km} km az {mertfold:.2f} mérföld.")

# ÉLES VERZIÓ:
# nev = input("Mi a neved? ").strip()

nev = "  Anna  "
print(f"Szóközökkel:    |{nev}|")
print(f"strip() után:   |{nev.strip()}|")


# -------------------------------------------------------------------------
# FELADATOK - 4. rész
# -------------------------------------------------------------------------
"""
8. feladat  ⭐  Kör területe
   Kérd be a sugarat input()-tal, és írd ki a kör területét
   két tizedesjegyre. (Terület = 3.14159 * r * r)
   A gyakorláshoz nyugodtan írd be a sugarat kézzel, ahogy fent
   csináltuk, de a bekérő sort is írd le kommentben.

9. feladat  ⭐⭐  Két szám
   Kérj be két számot, és írd ki az összegüket, a különbségüket és a
   szorzatukat, egy-egy mondatban, f-stringgel.
   Figyelj: az input() mindkét esetben szöveget ad vissza.
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# 5. RÉSZ - LISTÁK
# =========================================================================

cim("5. RÉSZ - LISTÁK  (20 perc)")

print("""
EMLÉKEZTETŐ - a bevásárlólista a hűtőn
--------------------------------------
  A változó egy doboz, amiben EGY dolog van. A lista egy doboz,
  amiben SOK dolog van, sorban.

      bevasarlas = ["tej", "kenyér", "tojás"]

  Olyan, mint a hűtőre ragasztott bevásárlólista: írsz rá, kihúzol
  róla, átrendezed, és mindig tudod, hogy mi az első és mi az utolsó.

  SZÁMOZÁS - és itt az első meglepetés:

      bevasarlas[0]    ->  "tej"      az ELSŐ elem a 0. !
      bevasarlas[1]    ->  "kenyér"
      bevasarlas[-1]   ->  "tojás"    az utolsó, hátulról

  SZELETELÉS - [honnan:meddig], és a "meddig" NEM kerül bele:

      bevasarlas[0:2]  ->  ["tej", "kenyér"]
      bevasarlas[:2]   ->  ugyanaz, elejétől
      bevasarlas[1:]   ->  a másodiktól a végéig

  A LEGFONTOSABB MŰVELETEK:

      lista.append("sajt")      a végére
      lista.insert(0, "kávé")   adott helyre
      lista.remove("kenyér")    érték alapján kiveszi
      lista.pop()               az utolsót kiveszi ÉS visszaadja
      len(lista)                hány elem van benne
      "tej" in lista            benne van-e?  True / False

  ⚠️  KÉT CSALÁD, és ez órákat spórol:
        lista.sort()     HELYBEN rendez, és None-t ad vissza
        sorted(lista)    békén hagyja, ÚJ rendezett listát ad

      Ezért a  bevasarlas = bevasarlas.sort()  katasztrófa:
      a listád None lesz és eltűnik.

  💡  Ugyanez igaz az append()-re: sosem írjuk, hogy
      lista = lista.append("x").
""")

alcim("Nézd meg futás közben")
bevasarlas = ["tej", "kenyér", "tojás"]
print("eredeti        ->", bevasarlas)
print("bevasarlas[0]  ->", bevasarlas[0])
print("bevasarlas[-1] ->", bevasarlas[-1])
print("bevasarlas[:2] ->", bevasarlas[:2])
print("len()          ->", len(bevasarlas))
print("'tej' in ...   ->", "tej" in bevasarlas)

bevasarlas.append("sajt")
bevasarlas.insert(0, "kávé")
bevasarlas.remove("kenyér")
print("módosítva      ->", bevasarlas)

print("sorted(...)    ->", sorted(bevasarlas), "  <- új lista")
print("az eredeti     ->", bevasarlas, "  <- érintetlen")

szamok = [10, 20, 30, 40, 50]
print("szamok[2:4]    ->", szamok[2:4])
print("sum / max / min->", sum(szamok), max(szamok), min(szamok))


# -------------------------------------------------------------------------
# FELADATOK - 5. rész
# -------------------------------------------------------------------------
"""
10. feladat  ⭐  Lista építése
    Indulj ebből:  tanulok = ["Anna", "Béla", "Cili"]
    a) tedd a végére: "Dóra"
    b) tedd a lista elejére: "Ádám"
    c) vedd ki: "Béla"
    d) írd ki, hány tanuló maradt

11. feladat  ⭐  Indexelés és szeletelés
    Adott:  szamok = [3, 8, 12, 5, 20, 7]
    Írd ki külön-külön: az elsőt, az utolsót (a -1 használatával),
    az első hármat, az utolsó kettőt, és a 3-4-5. elemet.

12. feladat  ⭐⭐  Rendezés a rontás nélkül
    Adott:  arak = [990, 450, 1250, 700]
    a) írd ki rendezve, DE úgy, hogy az eredeti lista ne változzon
    b) bizonyítsd be: írd ki utána az eredetit is
    c) egy kommentben írd le, mi történne a  arak = arak.sort()  sorral
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# 6. RÉSZ - CIKLUSOK
# =========================================================================

cim("6. RÉSZ - CIKLUSOK (for, while)  (20 perc)")

print("""
EMLÉKEZTETŐ - a futószalag és a biztonsági őr
---------------------------------------------
  FOR CIKLUS = futószalag.
  A dobozok elhaladnak előtted, mindegyikkel ugyanazt csinálod, és
  amikor az utolsó elmegy, vége. Előre tudod, hány doboz van.

      for tanulo in tanulok:
          print(tanulo)

  Olvasd ki hangosan: "minden tanuloért a tanulok listában".
  Nem kell index, nem kell számláló. A Python odaadja magát a dolgot.

  range() = amikor nem lista kell, hanem számok:

      range(5)        ->  0 1 2 3 4        ⚠️ nulla, és az 5 KIMARAD
      range(1, 6)     ->  1 2 3 4 5
      range(0, 10, 2) ->  0 2 4 6 8        harmadik szám: lépésköz

  WHILE CIKLUS = biztonsági őr az ajtóban.
  Megnéz egy feltételt, és amíg az igaz, újra és újra beenged.

      while jelszo != "titok":
          jelszo = input("Jelszó: ")

  ⚠️  A while-ban a ciklusmagban meg KELL változnia annak, amit az őr
      néz. Ha nem, örökké körbe-körbe jársz (végtelen ciklus, Ctrl+C).

  A GYŰJTŐVÖDÖR MINTA - ezt egy életen át fogod használni:

      osszeg = 0                   üres vödör, a ciklus ELŐTT
      for n in range(1, 101):
          osszeg = osszeg + n      minden körben beledobsz
      print(osszeg)                a végén belenézel

  ⚠️  Ha a vödröt a cikluson BELÜL hozod létre, minden körben kiöntöd.

  💡  enumerate() adja a sorszámot is, ha tényleg kell:
          for i, nev in enumerate(tanulok, start=1):
  💡  break = azonnal kilép,  continue = ugrik a következő körre.
""")

alcim("for - végigmegyünk egy listán")
tanulok = ["Anna", "Béla", "Cili"]
for tanulo in tanulok:
    print("   ", tanulo)

alcim("for + enumerate - számozva")
for i, tanulo in enumerate(tanulok, start=1):
    print(f"    {i}. {tanulo}")

alcim("for + range - a gyűjtővödör")
osszeg = 0
for n in range(1, 101):
    osszeg = osszeg + n
print("1-től 100-ig az összeg:", osszeg)

alcim("while - amíg a feltétel igaz")
szamlalo = 3
while szamlalo > 0:
    print("   visszaszámlálás:", szamlalo)
    szamlalo = szamlalo - 1  # ⚠️ e nélkül végtelen ciklus
print("   Indulás!")

alcim("break és continue")
for n in range(1, 11):
    if n % 2 != 0:
        continue  # a páratlanokat átugorjuk
    if n > 6:
        break  # 6 fölött kilépünk
    print("   páros és <= 6:", n)


# -------------------------------------------------------------------------
# FELADATOK - 6. rész
# -------------------------------------------------------------------------
"""
13. feladat  ⭐  Számok
    a) írd ki az 1-től 10-ig a számokat, egyet egy sorba
    b) írd ki az 1-től 50-ig a számok összegét (gyűjtővödör minta)

14. feladat  ⭐  Számozott névsor
    Adott:  tanulok = ["Anna", "Béla", "Cili", "Dóra"]
    Írd ki őket így:   1. Anna
                       2. Béla ...
    NE használj saját számlálót. A Pythonnak van erre beépített
    megoldása.

15. feladat  ⭐⭐  Szűrés ciklussal
    Adott:  homerseklet = [12, 25, 31, 8, 19, 27, 33, 4]
    a) készíts egy ÚJ listát, amiben csak a 20 fölötti értékek vannak
    b) írd ki, hány ilyen nap volt
    c) írd ki a legmelegebb napot (max használatával)

16. feladat  ⭐⭐  while
    Írj egy ciklust, ami addig ismétlődik, amíg a "jelszo" változó
    értéke nem "titok". A gyakorláshoz a beolvasás helyett dolgozz egy
    előre megadott listából (pl. ["alma", "korte", "titok"]), az input()-os
    változatot pedig írd le kommentben.
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# 7. RÉSZ - IF / ELIF / ELSE
# =========================================================================

cim("7. RÉSZ - IF / ELIF / ELSE  (15 perc)")

print("""
EMLÉKEZTETŐ - ajtók egy folyosón
--------------------------------
  Végigmész egy folyosón, és sorban próbálod az ajtókat. Az ELSŐ,
  amelyik kinyílik, azon mész be - a többit meg sem nézed.

      if pontszam >= 90:
          jegy = "5"
      elif pontszam >= 75:
          jegy = "4"
      elif pontszam >= 60:
          jegy = "3"
      else:
          jegy = "1"

  ⚠️  A SORREND mindent eldönt. Ha a "60 fölött" ajtó van elöl, akkor
      a 95 pontos dolgozat is hármas lesz, mert a 95 is 60 fölött van,
      és az az ajtó nyílt ki először.

  ⚠️  =  és  ==  nem ugyanaz!
        =   "tedd bele"      (utasítás)
        ==  "ugyanaz?"       (kérdés)
      Az if-nek kérdés kell.

  ⚠️  Több külön if = több külön folyosó. Mindegyiket végigjárja.
      Egy if/elif/else = EGY folyosó, egy döntés.

  ÖSSZEKAPCSOLÁS:
      and    mindkettő igaz legyen
      or     elég, ha az egyik igaz
      not    megfordítja

  ⚠️  Az "and" két oldalán önálló, teljes kérdés kell:
        rossz:  if hom > 30 and < 35
        jó:     if hom > 30 and hom < 35
        szebb:  if 30 < hom < 35

  💡  Az üres lista, az üres szöveg és a 0 önmagában "hamis".
      Ezért írjuk azt, hogy  if lista:  a  len(lista) > 0  helyett.
""")

alcim("Nézd meg futás közben")


def jegy(pontszam):
    if pontszam >= 90:
        return "5"
    elif pontszam >= 75:
        return "4"
    elif pontszam >= 60:
        return "3"
    else:
        return "1"


for p in [95, 80, 62, 40]:
    print(f"    {p:>3} pont -> {jegy(p)}")

alcim("Két feltétel egyszerre")
hom = 32
if 30 < hom < 35:
    print("    meleg van")
elif hom >= 35:
    print("    hőség")
else:
    print("    elviselhető")

alcim("Amikor az üresség hamis")
lista = []
if lista:
    print("    van benne valami")
else:
    print("    a lista üres  (if lista: elég ennyi)")


# -------------------------------------------------------------------------
# FELADATOK - 7. rész
# -------------------------------------------------------------------------
"""
17. feladat  ⭐  Mozijegy
    Írj egy fuggvenyt:  jegyar(eletkor)
        3 év alatt         ingyenes (0)
        3 - 15 év          1200
        16 - 64 év         2500
        65 évtől           1500
    Próbáld ki ezekkel: 2, 10, 30, 70.

18. feladat  ⭐⭐  Szerdai kedvezmény
    Bővítsd az előzőt:  jegyar(eletkor, nap)
    Szerdán MINDEN fizetős jegy 500 Ft-tal olcsóbb.
    Figyelj: az ingyenes maradjon ingyenes, ne legyen -500.
    Próbáld ki: (5, "hétfő"), (30, "szerda"), (70, "szerda"), (2, "szerda").
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# 8. RÉSZ - HIBAKEZELÉS (TRY / EXCEPT)
# =========================================================================

cim("8. RÉSZ - HIBAKEZELÉS (try / except)  (15 perc)")

print("""
EMLÉKEZTETŐ - a védőháló a trapéz alatt
---------------------------------------
  A try/except nem akadályozza meg az esést. Azt akadályozza meg,
  hogy az esés véget vessen az előadásnak.

      try:
          eletkor = int("alma")          <- ez elszáll
      except ValueError:
          print("Ez nem szám.")          <- ide ugrunk
      print("A program megy tovább.")

  A LEGGYAKORIBB HIBATÍPUSOK:

      ValueError          int("alma")        - jó fajta, rossz tartalom
      TypeError           "szöveg" + 5       - eleve rossz fajta
      ZeroDivisionError   10 / 0
      IndexError          [1, 2, 3][5]       - nincs ilyen sorszám
      KeyError            {"a": 1}["b"]      - nincs ilyen kulcs
      FileNotFoundError   nem létező fájl megnyitása

  ⚠️  Mindig NEVEZD MEG, milyen hibát vársz. A csupasz  except:
      mindent elkap - a saját elgépeléseidet is -, és egy ötperces
      javításból délutáni nyomozás lesz.

  ⚠️  Csak azt a sort tedd a try-ba, ami tényleg elszállhat.

  💡  A teljes szerkezet:
          try:      amit megpróbálunk
          except:   ha elszállt
          else:     ha NEM szállt el
          finally:  mindenképp lefut (pl. fájl bezárása)
""")

alcim("Nézd meg futás közben")

# ÉLES VERZIÓ:
# szoveg = input("Kérek egy számot: ")

for szoveg in ["42", "alma"]:
    try:
        szam = int(szoveg)
        print(f"    '{szoveg}' -> {szam}, a duplája {szam * 2}")
    except ValueError:
        print(f"    '{szoveg}' -> ez nem szám, kihagyom")

print("    A program tovább fut.")

alcim("Melyik hiba melyik")
probak = [
    ("int('alma')", lambda: int("alma")),
    ("10 / 0", lambda: 10 / 0),
    ("[1,2,3][5]", lambda: [1, 2, 3][5]),
    ("'szöveg' + 5", lambda: "szöveg" + 5),
]
for leiras, muvelet in probak:
    try:
        muvelet()
    except Exception as e:
        print(f"    {leiras:<14} -> {type(e).__name__}")


# -------------------------------------------------------------------------
# FELADATOK - 8. rész
# -------------------------------------------------------------------------
"""
19. feladat  ⭐  Elkapás
    Írj egy programot, ami megpróbálja számmá alakítani a "huszonöt"
    szöveget. Ha nem sikerül, írja ki: "Ez nem szám." - és utána még
    írjon ki egy sort, bizonyítva, hogy nem állt le.

20. feladat  ⭐⭐  Piszkos adat
    Adott:  meresek = ["12", "8", "alma", "31", "", "19", "0", "25"]
    Menj végig rajta, és:
      - alakítsd számmá az elemeket
      - a rosszaknál írj figyelmeztetést, benne a rossz értékkel
      - a jókat gyűjtsd egy listába
      - a végén írd ki: hány jó, hány rossz, az összeg, az átlag
        (egy tizedesre) és a legnagyobb
      - ha egyetlen jó érték sincs, "Nincs használható mérés." legyen
        a válasz, ne pedig egy nullával osztás
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# 9. RÉSZ - FÁJLKEZELÉS
# =========================================================================

cim("9. RÉSZ - FÁJLKEZELÉS  (20 perc)")

print("""
EMLÉKEZTETŐ - a füzet a fiókban
-------------------------------
  Eddig minden, amit a programod csinált, eltűnt, amint kilépett.
  A fájl egy füzet a fiókban: kiveszed, írsz bele, visszateszed -
  és holnap is ott lesz.

  Három dolgot kell eldöntened, amikor kinyitod:

      "r"   read      olvasom      ⚠️ hiba, ha nincs ilyen fájl
      "w"   write     írom         ⚠️ a RÉGI TARTALMAT KITÖRLI!
      "a"   append    hozzáfűzöm   a végére ír, a régit meghagyja

  A szabványos forma:

      with open("jegyzet.txt", "w", encoding="utf-8") as f:
          f.write("első sor\\n")

  A "with" a fontos rész: ez zárja be a fájlt helyetted, akkor is, ha
  közben hiba történik. Olyan, mint egy ajtó, ami magától becsukódik.

  ⚠️  encoding="utf-8" nélkül az ékezetek elromolhatnak. Mindig írd ki.
  ⚠️  A "\\n" a sortörés. Enélkül minden egymás után folyik.
  ⚠️  A "w" mód az első karakter leírása előtt kiüríti a fájlt.
      Ha hozzá akarsz tenni, az "a" kell.

  OLVASÁS - három módja:

      f.read()          az EGÉSZ tartalom egy szövegként
      f.readlines()     lista, soronként (a sorvégi \\n bennemarad)
      for sor in f:     soronként, memóriakímélően - ez a szokásos

  💡  A .strip() leszedi a sor végéről a felesleges sortörést.
  💡  os.path.exists("fajl.txt") megmondja, létezik-e - de gyakran
      egyszerűbb megpróbálni és elkapni a FileNotFoundError-t.
""")

alcim("Írás - létrehozunk egy fájlt")
with open("jegyzet.txt", "w", encoding="utf-8") as f:
    f.write("tej\n")
    f.write("kenyér\n")
    f.write("tojás\n")
print("    jegyzet.txt létrehozva, 3 sorral")

alcim("Hozzáfűzés - a régi megmarad")
with open("jegyzet.txt", "a", encoding="utf-8") as f:
    f.write("sajt\n")
print("    hozzáfűzve: sajt")

alcim("Olvasás - soronként")
with open("jegyzet.txt", "r", encoding="utf-8") as f:
    for sorszam, sor in enumerate(f, start=1):
        print(f"    {sorszam}. {sor.strip()}")

alcim("Olvasás - listába")
with open("jegyzet.txt", "r", encoding="utf-8") as f:
    sorok = [sor.strip() for sor in f]
print("    sorok listája ->", sorok)
print("    sorok száma   ->", len(sorok))

alcim("Ha nincs ilyen fájl - a 8. rész munkában")
try:
    with open("nincs_ilyen.txt", "r", encoding="utf-8") as f:
        f.read()
except FileNotFoundError:
    print("    FileNotFoundError elkapva - a program megy tovább")

# takarítás, hogy a mappa rendes maradjon
if os.path.exists("jegyzet.txt"):
    os.remove("jegyzet.txt")


# -------------------------------------------------------------------------
# FELADATOK - 9. rész
# -------------------------------------------------------------------------
"""
21. feladat  ⭐  Első fájlod
    a) hozz létre egy "tanulok.txt" fájlt, és írj bele négy nevet,
       mindegyiket külön sorba
    b) olvasd vissza, és írd ki a neveket számozva

22. feladat  ⭐⭐  Hozzáfűzés és számolás
    a) fűzz hozzá a "tanulok.txt"-hez még két nevet ("a" mód)
    b) olvasd vissza a fájlt, és írd ki, hány név van benne
    c) írd ki csak azokat a neveket, amik "A" betűvel kezdődnek
       (💡 a .startswith("A") segít)

23. feladat  ⭐⭐  Biztonságos olvasás
    Írj egy  beolvas(fajlnev)  függvényt, ami visszaadja a fájl
    sorait listaként. Ha a fájl nem létezik, ne szálljon el: írja ki,
    hogy "Nincs ilyen fájl: ...", és adjon vissza üres listát.
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# ZÁRÓFELADAT (capstone)
# =========================================================================
"""
24. feladat  ⭐⭐⭐  Hőmérséklet-napló
    Egy programot írsz, ami mind a kilenc mai témát használja.

    Kiindulás:
        nyers = ["12", "8", "alma", "31", "", "19", "0", "25"]

    A program:
      1. menjen végig a nyers listán, és alakítsa számmá az elemeket
         (típuskonverzió + hibakezelés)
      2. a rossz elemeket hagyja ki, de írjon róluk figyelmeztetést,
         benne a rossz értékkel (f-string)
      3. a jó értékeket gyűjtse egy listába (lista + ciklus)
      4. minden értékhez tegyen egy címkét if/elif/else-szel:
             20 fölött   -> "meleg"
             10 - 20     -> "enyhe"
             10 alatt    -> "hideg"
      5. írja ki a képernyőre az összesítést: hány jó, hány rossz,
         átlag egy tizedesre, legmagasabb, legalacsonyabb
      6. MENTSE az egészet egy "naplo.txt" fájlba, soronként így:
             25 fok - meleg
         és a fájl végére írja oda az összesítést is
      7. végül olvassa vissza a fájlt, és írja ki a tartalmát,
         bizonyítva, hogy tényleg elmentődött
      8. ha a fájl megnyitása nem sikerül, kapja el a hibát és írjon
         értelmes üzenetet

    💡 Bontsd fel függvényekre, ha már tanultál függvényt. Ha még nem,
       egyetlen, felülről lefelé olvasható program is teljesen jó.
"""

# TODO: ide írd a megoldást
pass


# =========================================================================
# AMIT MA GYAKOROLTUNK
# =========================================================================

cim("AMIT MA GYAKOROLTUNK")

print("""
  1. VÁLTOZÓ        felcímkézett doboz;  =  azt jelenti: "tedd bele"

  2. TÍPUSOK        "5" kártya, 5 érme.  int() / float() / str()
                    int(3.9) levág, round(3.9) kerekít

  3. F-STRING       f"{nev} {kor} éves"  -  az f a nyitó idézőjel előtt
                    f"{ar:.2f}"  két tizedesre

  4. INPUT          postaláda: MINDIG szöveget ad.
                    int(input(...)) - alakíts az ajtóban

  5. LISTA          sorban álló dobozok; a számozás 0-ról indul
                    lista.sort() helyben rendez és None-t ad vissza,
                    sorted(lista) új listát ad

  6. CIKLUS         for = futószalag (ismert számú elem)
                    while = őr az ajtóban (amíg a feltétel igaz)
                    gyűjtővödör: a vödröt a ciklus ELŐTT hozd létre

  7. IF / ELIF      ajtók a folyosón, az első nyíló ajtó nyer
                    a sorrend dönt;  =  betesz,  ==  kérdez

  8. TRY / EXCEPT   védőháló, nem vakfolt.
                    nevezd meg a hibát: except ValueError:

  9. FÁJL           füzet a fiókban.  with open(..., encoding="utf-8")
                    "w" TÖRÖL, "a" hozzáfűz, "r" olvas

  HA MA CSAK ÖT DOLGOT VISZEL HAZA
    1. Az input() szöveget ad. Alakítsd át azonnal.
    2. A lista első eleme a [0].
    3. A sorted() új listát ad, a .sort() nem ad vissza semmit.
    4. Az if/elif sorrendje a logikád - nem díszítés.
    5. A "w" mód kitörli a fájlt. Az "a" nem.
""")

print("\nKövetkező lecke: függvények, szótárak (dict) és a listakifejezés.\n")
