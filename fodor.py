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

def fodor1feladat(lista):
    listasd = []
    for elem in lista:
        if elem.orszag == "Magyarország":
            listasd.append((f"{elem.helyezes} ,  {elem.ev} ,  {elem.helyszin}"))
    return listasd

print(fodor1feladat(Csapat.lista))