def rot13(palabra):
    L1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    L2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    S1="".join(L1)
    S2="".join(L2)
    l=list(palabra)
    n=0
    while n<=len(palabra)-1:
        if S1.find(l[n])!=-1:
            l[n]=L2[S1.find(l[n])]
            palabra="".join(l)
            n+=1
        elif S2.find(l[n])!=-1:
            l[n]=L1[S2.find(l[n])]
            palabra="".join(l)
            n+=1
        else:
            n+=1
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           