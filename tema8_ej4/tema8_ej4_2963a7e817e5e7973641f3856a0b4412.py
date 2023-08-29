def rot13(palabra):
    normal=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    rot13=["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    codif=""
    for a in range(len(palabra)):
        codif+=rot13[normal.index(palabra[a])]
    return codif

           