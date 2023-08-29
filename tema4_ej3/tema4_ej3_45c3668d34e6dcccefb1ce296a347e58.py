def jerigonzo(string):
    p=""
    for l in string:
        l=str(l)
        if (l)=="a":
            p=p+"apa"
        elif l=="e":
            p=p+"epe"
        elif l=="i":
            p=p+"ipi"
        elif l=="o":
            p=p+"opo"
        elif l=="u":
            p=p+"upu"
        else:
            p=p+l
    string=p
    return string
