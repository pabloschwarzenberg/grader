def rot13(palabra):
    abc = ["a", "b", "c", "d","e","f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w"
            , "x", "y", "z" , "a", "b", "c", "d","e","f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w"
            , "x", "y", "z" ]
    conta = 0
    contb = 0
    palabra_list = []
    while conta < len(palabra):
        palabra_list.append(palabra[conta])
        conta += 1
    while contb < len(palabra):
        lugar = abc.index(palabra_list.pop(contb))
        new = abc[lugar+13]
        palabra_list.insert(contb, new)
        contb += 1
    palabra = "".join(str(x) for x in palabra_list)
    return palabra


if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)

