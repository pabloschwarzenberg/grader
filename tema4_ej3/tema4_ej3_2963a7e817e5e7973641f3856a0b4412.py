def jerigonzo (string):
    palabra=""
    for a in range(len(string)):
        p="p"
        palabra+=string[a]
        vocales=["a","e","i","o","u","A","E","I","O","U"]
        if string[a] in vocales:
            palabra+=p
            palabra+=string[a].lower()
    return palabra
