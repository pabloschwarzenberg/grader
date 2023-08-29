
def jerigonzo(string):
    palabra = ""
    for l in string:
        l = str(l)
        if (l) == "a":
            palabra = palabra+"apa"
        elif l == "e":
            palabra = palabra+"epe"
        elif l == "i":
            palabra = palabra+"ipi"
        elif l == "o":
            palabra = palabra+"opo"
        elif l == "u":
            palabra = palabra+"upu"
        else:
            palabra = palabra+l
    string = palabra
    return string