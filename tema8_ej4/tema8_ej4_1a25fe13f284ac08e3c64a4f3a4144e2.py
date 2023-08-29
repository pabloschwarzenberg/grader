def rot13(palabra):
    palabra=palabra.lower()
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    rot=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    i=""
    for l in palabra:
        if l in abc:
            r=abc.index(l)
            i=i+rot[r]
        if l in rot:
            r=rot.index(l)
            i=i+abc[r]
        if l=="":
            i=i+abc
    return(i)

           