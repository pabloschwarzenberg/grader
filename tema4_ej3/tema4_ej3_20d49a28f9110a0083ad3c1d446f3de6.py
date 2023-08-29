def jerigonzo(string):
    Palabra=""
    for l in string:
        l=str(l)
        if (l)=="a":
            Palabra=Palabra+"apa"
        elif l=="e":
            Palabra=Palabra+"epe"
        elif l=="i":
            Palabra=Palabra+"ipi"
        elif l=="o":
            Palabra=Palabra+"opo"
        elif l=="u":
            Palabra=Palabra+"upu"
        else:
            Palabra=Palabra+l
    string=Palabra
    return string