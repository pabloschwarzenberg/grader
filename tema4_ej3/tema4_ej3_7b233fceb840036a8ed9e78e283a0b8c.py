def jerigonzo(string):
    palabras=""
    for l in string:
        l=str(l)
        if (l)=="a":
            palabras=palabras+"apa"
        elif l=="e":
            palabras=palabras+"epe"
        elif l=="i":
            palabra=palabra+"ipi"
        elif l=="o":
            palabras=palabras+"opo"
        elif l=="u":
            palabras=palabras+"upu"
        else:
            palabras=palabras+l
    string=palabras
    return string