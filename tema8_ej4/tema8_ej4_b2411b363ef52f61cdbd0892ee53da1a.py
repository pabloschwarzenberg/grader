def rot13(palabra):
    u=list(palabra)
    l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    j=["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    m=[]
    for i in range(0,len(u)):
        a=l.index(u[i])
        nuevo=j[a]
        m.append(nuevo)
    return "".join(m)
           