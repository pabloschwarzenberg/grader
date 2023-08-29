def jerigonzo(string):
    convertido = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertido.append(letra)
    convertido = "".join(convertido)
    return convertido

def rot13(txt):
    cifrado = ""
    desplazamiento = 13
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(txt)):
        for j in range(len(letras)):
            if txt[i] == letras[j]:
                if j + desplazamiento > 25:
                    diff = (j + desplazamiento) - 25
                    cifrado = cifrado + (letras[diff -1])
                else:
                    cifrado = cifrado + (letras[j+desplazamiento])
    return cifrado
