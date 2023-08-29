def jerigonzo(palabra):
    palabra.lower()
    L=list(palabra)
    i=0
    while i < len(L):
        if L[i]=="a" or L[i]=="e" or L[i]=="i" or L[i]=="o" or L[i]=="u":
            L[i]=L[i]+"p"+L[i]
            i=i+1
        else:
            i=i+1

    palabra="".join(L)
    return palabra