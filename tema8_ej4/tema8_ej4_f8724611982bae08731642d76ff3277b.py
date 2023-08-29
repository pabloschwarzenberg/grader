def rot13(palabras):
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    largo=len(palabras)
    for i in range(0,largo):
        posicion=alfabeto.index(palabras[i])
        if posicion<=12:
            a=palabras[i]
            b=alfabeto[posicion+13]
            #palabras=palabras.replace(a,b)
            n=list(palabras)
            n.pop(i)
            n.insert(i,b)
            print(n)
            palabras="".join(n)
        elif posicion>=13:
            a=palabras[i]
            b=alfabeto[posicion-13]
            #palabras=palabras.replace(a,b)
            n=list(palabras)
            n.pop(i)
            n.insert(i,b)
            print(n)
            palabras="".join(n)
    return palabras
 


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           