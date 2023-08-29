abcedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def rot13(palabra):
    palabra = list(palabra)
    for i in range(len(palabra)):
        print(i)
        j = palabra[i]
        print(j)
        posicion = abcedario.index(j)
        print(posicion)
        posicion += 13
        if posicion >= 26:
            posicion -= 26
        print(posicion)
        palabra[i] = abcedario[posicion]
    palabra_rot = "".join(palabra)
    return palabra_rot


if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
