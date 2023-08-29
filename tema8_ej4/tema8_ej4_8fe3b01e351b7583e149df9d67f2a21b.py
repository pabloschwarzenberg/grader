def rot13(palabra):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for i in palabra:
        if i in alfabeto:
            if alfabeto.index(i) < 13:
                string += alfabeto[alfabeto.index(i) + 13]
            else:
                string += alfabeto[alfabeto.index(i) - 13]

        elif i in alfabeto.upper():
             if alfabeto.upper().index(i) < 13:
                 string += alfabeto.upper()[alfabeto.upper().index(i) + 13]
             else:
                string += alfabeto.upper()[alfabeto.upper().index(i) - 13]
        else:
            string += 1

    return string

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)