# 42)	A program olvasson be egy csapat nevet és írja ki, a csapat vb-n elért legjobb helyezését!

def feladat_42(lista):
    temp = input()
    temp2 = 100
    for i in lista:
        if i.orszag == temp:
            if i.helyezes < temp2:
                temp2 = i.helyezes
    return temp2

# 43)	A program olvasson be egy csapat nevet és írja ki, a csapat hányszor nyert vb-t!

def feladat_43(lista):
    temp = input()
    temp2 = 0
    for i in lista:
        if i.orszag == temp:
            if i.helyezes == 1:
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

