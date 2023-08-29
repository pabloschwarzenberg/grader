def jerigonzo(string):
    posicion=0
    palabra=[]
    vocales=["a","e","i","o","u"]
    #print(len(string))
    while posicion<len(string):
        for letra in string:
            if letra in vocales:
                palabra.append(letra+"p"+letra)
            else:
                palabra.append(letra)
            posicion+=1
        palabra="".join(palabra)
        return palabra

if __name__ == "__main__":
    pass
         