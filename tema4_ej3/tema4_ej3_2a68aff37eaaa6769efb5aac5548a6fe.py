def jeringozo (string):
    
    convert=[]
    for palabra in string :
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p" + letra
            convert.append(letra)
    convert = "".join(convert)
    return convert

if __name__ == "__main__":
    pass


