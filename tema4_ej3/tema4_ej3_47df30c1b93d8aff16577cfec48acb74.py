def jerigonzo(string):
    pal_convertida = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            pal_convertida.append(letra)
    convertido = "".join(pal_convertida)
    return convertido
    
