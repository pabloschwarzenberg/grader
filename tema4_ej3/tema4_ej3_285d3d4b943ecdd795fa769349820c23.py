def jerigonzo(string):
    palabra = []
    letras = str("aeiouAEIOU")
    for p in string:
        for l in p:
            if l in letras:
                l = l + "p" + l
            palabra.append(l)
    palabra = "".join(palabra)
    
    return palabra

if __name__ == "__main__":
    pass
         