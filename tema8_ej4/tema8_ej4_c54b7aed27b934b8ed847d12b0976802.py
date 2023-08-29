def rot13(p):
    l1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    l2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra=list(p)
    k=0
    while k<len(palabra):
        if palabra[k] in l1:
            palabra[k]=l2[l1.index(palabra[k])]
        elif palabra[k] in l2:
            palabra[k]=l1[l2.index(palabra[k])]
        k=k+1
    pala=""
    for l in palabra:
        pala=pala+l
    return pala
    pass
if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)