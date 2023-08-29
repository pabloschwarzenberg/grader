def jeringonzo(string):
    convertido=[]
    for palabra in string:
        if letra in "aeiouAEIOU":
            letra=letra+"p"+letra
        convertido.append(letra)
    convertido= "".join(convertido)
    return convertido