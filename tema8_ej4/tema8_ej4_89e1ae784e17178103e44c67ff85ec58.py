def rot13(palabra):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    s=""
    for i in range(0, len(palabra)):
        a = alfabeto.index(palabra[i]) # a la letra que esta en la palabra,le saco la posicion dentro del alfabeto

        if a < 13:
            s=s+ (alfabeto[a + 13]) #le busco la letra que esta 13 posiciones mas alla y lo voy uniendo a un string vacio
        else:
            s=s+ (alfabeto[a-13])
    return s   #retorno el string que es mi palabra codificada

    pass


if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)