# 42)	A program olvasson be egy csapat nevet és írja ki, a csapat vb-n elért legjobb helyezését!

def feladat_42(lista):
    temp = input()
    temp2 = 100
    for i in lista:
        if i.orszag == temp:
            if i.helyezes < temp2:
                temp2 = i.helyezes
    return temp2
