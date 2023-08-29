def jerigonzo(palabra):
    lista=list(palabra)
    vocales=["a","e","i","o","u"]
    vocales2="aeiou"
    contar=0
    for i in palabra:
        for p in vocales:
            if i==p:
                posicion_vocal=lista.index(p)
                lista[posicion_vocal]=p+"p"+p
            elif vocales2.find(i)==-1:
                break

    palabra="".join(lista)
    return palabra
print(jerigonzo("estamos programando"))


         