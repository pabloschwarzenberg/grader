def rot13(palabra):
    n=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    i=0
    k=0
    palabra=list(palabra)
    while i<len(palabra):
        while k<len(n):
            if k<13:
                if (n[k] in palabra[i])==True:
                    palabra[i]=n[k+13]
                    break
            elif k==13:
                if (n[k] in palabra[i])==True:
                    palabra[i]=n[0]
                    break
            else:
                if (n[k] in palabra[i])==True:
                    palabra[i]=n[k-13]
                    break
            k=k+1
                    
        k=0
        i=i+1
    palabra="".join(palabra)    
    return palabra    
if __name__=="__main__":
    palabra=str(input("Ingresa la palabra que quieras encriptar: "))
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           
