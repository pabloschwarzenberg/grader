def rot13(palabra):
    letras = "abcdefghijklmnopqrstuvwxyz"
    mensaje_final = ""
    for indice in range(len(palabra)):
        posicion = 0
        for indice_j in range(len(letras)):
            if palabra[indice] == letras[indice_j]:
                posicion = indice_j 
                print(posicion)
                break
        try:
            mensaje_final += letras[posicion+13]
        except:
            mensaje_final += letras[posicion-13]

    return mensaje_final

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           