class Csapat:
    lista = []
    def __init__(self, sorszam, orszag, helyezes, ev, helyszin):
        self.sorszam = sorszam
        self.orszag = orszag
        self.helyezes = helyezes
        self.ev = ev
        self.helyszin = helyszin
        Csapat.lista.append(self)

with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split("\t")
        t = Csapat(int(s[0]), s[1], int(s[2]), int(s[3]), s[4])

def feladat_1_6(lista, ország):
    for elem in lista:
        if elem.orszag == ország:
            print(f"{elem.helyezes}  {elem.ev}  {elem.helyszin}")

print("----------------------------------------------------------------")
print("1.Feladat")
feladat_1_6(Csapat.lista, "Magyarország")
print("----------------------------------------------------------------")
print("2.Feladat")
feladat_1_6(Csapat.lista, "Anglia")
print("----------------------------------------------------------------")
print("3.Feladat")
feladat_1_6(Csapat.lista, "Chile")
print("----------------------------------------------------------------")
print("4.Feladat")
feladat_1_6(Csapat.lista, "Peru")
print("----------------------------------------------------------------")
print("5.Feladat")
feladat_1_6(Csapat.lista, "Mongolia")
print("----------------------------------------------------------------")
print("6.Feladat")
feladat_1_6(Csapat.lista, input("Adj meg egy csapatnevet: "))

def feladat_7_12(lista, évtized):
    for elem in lista:
        if elem.helyezes == 1 and (elem.ev - 1900 >= évtized and elem.ev - 1900 < évtized + 10):
            print(f"{elem.orszag}  {elem.ev}")

print("----------------------------------------------------------------")
print("7.Feladat")
feladat_7_12(Csapat.lista, 30)
print("----------------------------------------------------------------")
print("8.Feladat")
feladat_7_12(Csapat.lista, 40)
print("----------------------------------------------------------------")
print("9.Feladat")
feladat_7_12(Csapat.lista, 50)
print("----------------------------------------------------------------")
print("10.Feladat")
feladat_7_12(Csapat.lista, 60)
print("----------------------------------------------------------------")
print("11.Feladat")
feladat_7_12(Csapat.lista, 70)
print("----------------------------------------------------------------")
print("12.Feladat")
feladat_7_12(Csapat.lista, 80)

def feladat_13_18(lista, ország):
    sum = 0;
    for elem in lista:
        if elem.orszag == ország:
            #print(f"{elem.orszag}  {elem.helyezes}  {elem.ev}  {elem.helyszin}")
            sum += 1
    print(sum)

print("----------------------------------------------------------------")
print("13.Feladat")
feladat_13_18(Csapat.lista, "Magyarország")
print("----------------------------------------------------------------")
print("14.Feladat")
feladat_13_18(Csapat.lista, "Anglia")
print("----------------------------------------------------------------")
print("15.Feladat")
feladat_13_18(Csapat.lista, "Chile")
print("----------------------------------------------------------------")
print("16.Feladat")
feladat_13_18(Csapat.lista, "Peru")
print("----------------------------------------------------------------")
print("17.Feladat")
feladat_13_18(Csapat.lista, "Mongólia")
print("----------------------------------------------------------------")
print("18.Feladat")
feladat_13_18(Csapat.lista, input("Adj meg egy csapatnevet: "))

def feladat_19_23(lista, év):
    for elem in lista:
        if elem.ev == év and elem.helyezes == 1:
            print(f"{elem.orszag}")

print("----------------------------------------------------------------")
print("19.Feladat")
feladat_19_23(Csapat.lista, 1930)
print("----------------------------------------------------------------")
print("20.Feladat")
feladat_19_23(Csapat.lista, 1940)
print("----------------------------------------------------------------")
print("21.Feladat")
feladat_19_23(Csapat.lista, 1950)
print("----------------------------------------------------------------")
print("22.Feladat")
feladat_19_23(Csapat.lista, 1960)
print("----------------------------------------------------------------")
print("23.Feladat")
feladat_19_23(Csapat.lista, 1970)