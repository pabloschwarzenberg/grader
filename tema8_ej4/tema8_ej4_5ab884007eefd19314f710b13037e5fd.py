def rot13(palabra):
    a=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    n=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra=list(palabra)
    for i in range(len(palabra)):
        for j in range(0,13):
            if a[j]==palabra[i]:
                palabra.insert(i,n[j])
                palabra.pop(i+1)
            elif n[j]==palabra[i]:
                palabra.insert(i,a[j])
                palabra.pop(i+1)
    palabra="".join(palabra)
    return palabra

    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           