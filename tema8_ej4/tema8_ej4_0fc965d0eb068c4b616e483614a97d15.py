def rot13(palabra):
    abc = "abcdefghijklm"
    nop = "nopqrstuvwxyz"
    frase = ""

    for letra in palabra:
        if letra in abc:
            for i in range(13):
                if letra == abc[i]:
                    frase += nop[i]
        elif letra in nop:
            for i in range(13):
                if letra == nop[i]:
                    frase += abc[i]
        else:
            frase += letra

    return frase

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
