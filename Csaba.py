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
