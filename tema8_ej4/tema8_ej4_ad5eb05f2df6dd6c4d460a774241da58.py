def rot13(palabra):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    codigo="nopqrstuvwxyzabcdefghijklm"
    nPalabra=""
    y=0
    for x in palabra:
        y=alfabeto.find(x)
        nPalabra+=codigo[y]
    return nPalabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           