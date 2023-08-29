
def jerigonzo(string):
    vocal = ["a", "A", "e", "E" "i", "I", "o", "O", "u", "U"]
    convertido = []
    for palabra in string:
        for letra in palabra:
            if letra in vocal:
                letra = letra + "p"+ letra
            convertido.append(letra)
    convertido = "".join(convertido)
    return convertido