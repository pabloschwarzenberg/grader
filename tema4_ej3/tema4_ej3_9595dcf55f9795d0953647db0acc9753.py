def jerigonzo(string):
    convertido = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertido.append(letra)
    convertido = "".join(convertido)
    return convertido
if __name__ == "__main__":
    palabra = eval(input("Ingrese una palabra para traducir a jerigonzo: "))
    Jerigonzo(palabra)
    pass
    
         