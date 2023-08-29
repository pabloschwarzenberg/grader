def rot13 (palabra):
    palabra=palabra.lower()
    L=["a","b","c","d","e","f","g","h","i","j","k","l","m"," "]
    rot=["n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    i=""
    for l in palabra:
        if l in L:
            r=L.index(l)
            i=i+rot[r]
        if l in rot:
            r=rot.index(l)
            i=i+L[r]
        if l=="":
            i=i+L
    return(i)
