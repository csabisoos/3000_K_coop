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

def feladat_24(lista):
    x = 0
    for elem in lista:
        if elem.helyezes == 2 and elem.orszag == "Magyarország":
            x += 1
    return x

def feladat_25(lista):
    x = 0
    for elem in lista:
        if elem.helyezes == 2 and elem.orszag == "Mongólia":
            x += 1
    return x

def feladat_26(lista):
    x = 0
    for elem in lista:
        if elem.helyezes == 2 and elem.orszag == "Svájc":
            x += 1
    return x

def feladat_27(lista):
    x = 0
    for elem in lista:
        if elem.helyezes == 2 and elem.orszag == "Brazília":
            x += 1
    return x

def feladat_28(lista):
    x = 0
    for elem in lista:
        if elem.helyezes == 2 and elem.orszag == "Németország":
            x += 1
    return x

def feladat_29(lista):
    x = 0
    for elem in lista:
        if elem.helyezes == 2 and elem.orszag == "Argentína":
            x += 1
    return x

def feladat_30(lista):
    x = input("Adjon meg egy évszámot és megmondom melyik csapat nyert az adott évben.\n")
    for elem in lista:
        if elem.ev == int(x) and elem.helyezes == 1:
            return elem.orszag
        
def feladat_31(lista):
    x = lista[0].ev
    for elem in lista:
        if elem.ev < x:
            x = elem.ev
    return x

def feladat_32(lista):
    x = 0
    for elem in lista:
        if elem.orszag == "Magyarország" and elem.helyezes == 1:
            x += 1
    return x

def feladat_33(lista):
    x = 0
    for elem in lista:
        if elem.orszag == "Anglia" and elem.helyezes == 1:
            x += 1
    return x

def feladat_34(lista):
    x = 0
    for elem in lista:
        if elem.orszag == "Chile" and elem.helyezes == 1:
            x += 1
    return x

def feladat_35(lista):
    x = 0
    for elem in lista:
        if elem.orszag == "Peru" and elem.helyezes == 1:
            x += 1
    return x

def feladat_36(lista):
    x = 0
    for elem in lista:
        if elem.orszag == "Mongólia" and elem.helyezes == 1:
            x += 1
    return x

def feladat_37(lista):
    x = 100
    for elem in lista:
        if elem.orszag == "Magyarország" and elem.helyezes < x:
            x = elem.helyezes
    return x
        
def feladat_38(lista):
    x = 100
    for elem in lista:
        if elem.orszag == "Anglia" and elem.helyezes < x:
            x = elem.helyezes
    return x
    
def feladat_39(lista):
    x = 100
    for elem in lista:
        if elem.orszag == "Chile" and elem.helyezes < x:
            x = elem.helyezes
    return x

def feladat_40(lista):
    x = 100
    for elem in lista:
        if elem.orszag == "Peru" and elem.helyezes < x:
            x = elem.helyezes
    return x

def feladat_41(lista):
    x = 100
    for elem in lista:
        if elem.orszag == "Mongólia" and elem.helyezes < x:
            x = elem.helyezes
    return x

print(feladat_24(Csapat.lista))
print(feladat_25(Csapat.lista))
print(feladat_26(Csapat.lista))
print(feladat_27(Csapat.lista))
print(feladat_28(Csapat.lista))
print(feladat_29(Csapat.lista))
print(feladat_30(Csapat.lista))
print(feladat_31(Csapat.lista))
print(feladat_32(Csapat.lista))
print(feladat_33(Csapat.lista))
print(feladat_34(Csapat.lista))
print(feladat_35(Csapat.lista))
print(feladat_36(Csapat.lista))
print(feladat_37(Csapat.lista))
print(feladat_38(Csapat.lista))
print(feladat_39(Csapat.lista))
print(feladat_40(Csapat.lista))
print(feladat_41(Csapat.lista))
