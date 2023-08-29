def jerigonzo(palabra):
    vocales=["a","e","i","o","u"]
    l_palabra=[]
    for letra in palabra:
        if letra in vocales:
            posicion_letra=palabra.index(letra)
            parte1="".join(palabra[:posicion_letra+1])
            parte2="".join(palabra[posicion_letra+1:])
            l_palabra.append(parte1)
            palabra=parte2
    for i in range(len(l_palabra)):
        l_palabra[i]=l_palabra[i]+"p"+l_palabra[i][-1]
    palabra_final="".join(l_palabra)
    return palabra_final

if __name__ == "__main__":
    pass
         