from operator import contains

# 42)	A program olvasson be egy csapat nevet és írja ki, a csapat vb-n elért legjobb helyezését!

def feladat_42(lista):
    temp = input("Adjon meg egy csapat nevet: ")
    temp2 = 100
    for i in lista:
        if i.orszag == temp and i.helyezes < temp2:
            temp2 = i.helyezes
    return temp2

# 43)	A program olvasson be egy csapat nevet és írja ki, a csapat hányszor nyert vb-t!

def feladat_43(lista):
    temp = input("Adjon meg egy csapat nevet: ")
    temp2 = 0
    for i in lista:
        if i.orszag == temp and i.helyezes == 1:
            temp2 += 1
    return temp2

# 44)	Melyik csapatok nyertek az Angiában rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!

def IttNyertCsapatok(lista, ország):
    temp = []
    for i in lista:
        if i.helyszín == ország:
            temp.append((i.helyszín, i.ev))
    return temp

def feladat_44(lista):
    return IttNyertCsapatok(lista, "anglia")
    

# 45)	Melyik csapatok nyertek a Magyarországon rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!

def feladat_45(lista):
    return IttNyertCsapatok(lista, "Magyarország")

# 46)	Melyik csapatok nyertek a Németországban rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!

def feladat_46(lista):
    return IttNyertCsapatok(lista, "Németország")

# 47)	Melyik csapatok nyertek az Brazíliában rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!

def feladat_47(lista):
    return IttNyertCsapatok(lista, "Brazília")

# 48)	Melyik csapatok nyertek az Egyesült Államok rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!

def feladat_48(lista):
    return IttNyertCsapatok(lista, "Egyesült Államok")

# 49)	A program olvasson be egy ország nevet és írja ki, melyik csapatok nyertek az adott helyszínen! A csapatok neve mellett az évszámot is írja ki!

def feladat_49(lista):
    return IttNyertCsapatok(lista, input("Adjon meg egy ország nevet: "))

# 50)	Melyik csapat nyerte a vb-t, amikor Magyarország dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!

def VBtNyertAmikorXYDobogósLett(lista, ország):
    temp = []
    temp2 = []
    for i in lista:
        if i.orszag == ország and i.helyezes <=3 and 1 <= i.helyezes and not temp.contains(i.ev):
            temp.append(i.ev)
    for i in lista:
        for j in temp:
            if i.ev == j and i.helyezes == 1:
                temp2.append((i.orszag, i.ev))
    return temp2

def feladat_50(lista):
    return VBtNyertAmikorXYDobogósLett(lista, "Magyarország")

# 51)	Melyik csapat nyerte a vb-t, amikor Brazília dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!

def feladat_51(lista):
    return VBtNyertAmikorXYDobogósLett(lista, "Brazília")

# 52)	Melyik csapat nyerte a vb-t, amikor Argentína dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!

def feladat_52(lista):
    return VBtNyertAmikorXYDobogósLett(lista, "Argentína")