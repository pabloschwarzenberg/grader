def jerigonzo(string):
    lista=[]
    vocales="aeiou"
    for letra in string:
        lista.append(letra)
    for i in range(0,len(string)):
        if lista[i] in vocales:
            lista[i]=lista[i]+"p"+lista[i]
    return "".join(lista)

if __name__ == "__main__":
    pass
         