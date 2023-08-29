def rot13(palabra):
    a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    b=["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    l = []
    palabra=list(palabra)
    for i in range(0,len(palabra)):
      x = a.index(palabra[i])
      l.append(b[x])
    return("".join(l))
           