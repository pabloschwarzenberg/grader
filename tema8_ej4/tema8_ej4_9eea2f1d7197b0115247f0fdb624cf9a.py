def rot13(palabra):
    palabra1 = ""
    abecedario = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
    for i in range(0, len(palabra)):
        letra_palabra = palabra[i]
        posicion = abecedario.find(letra_palabra)
        nueva_posicion = posicion+13
        nueva_letra = abecedario[nueva_posicion]
        palabra1+=nueva_letra
    return palabra1

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           