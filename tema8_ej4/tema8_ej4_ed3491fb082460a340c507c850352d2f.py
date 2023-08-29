def rot13(palabra):
    lista = []
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
    b = len(alfabeto)
    for a in palabra:
        c = alfabeto.index(a)
        if c > 13:
            lista.append(alfabeto[(b - (c + 13))*(-1)])
        elif c <= 13:
            lista.append(alfabeto[c + 13])

    s = "".join(lista)
    return s


if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
