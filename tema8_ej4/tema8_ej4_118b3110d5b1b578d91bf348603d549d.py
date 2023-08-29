def rot13(palabra):
    trece1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    trece2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra = list(palabra)
    k = 0
    for i in palabra:
        if i in trece1:
            indice = trece1.index(i)
            palabra[k] = trece2[indice]
            k += 1
        elif i in trece2:
            indice = trece2.index(i)
            palabra[k] = trece1[indice]
            k += 1
    e = ""
    for u in palabra:
        e += u
    palabra = e
    return palabra

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ",resultado)
           