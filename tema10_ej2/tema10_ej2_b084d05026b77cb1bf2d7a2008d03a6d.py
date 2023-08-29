#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1 == palabra2:
        distancia = "0D"
    elif len(palabra1)== len(palabra2):
        distancia = sustituir(palabra1, palabra2)
    elif abs(len(palabra1) - len(palabra2)) >= 1:
        distancia = insertar_borrar(palabra1, palabra2)
    return distancia


 
def insertar_borrar(palabra1, palabra2):
    status = "+1"
    a= len(palabra1)
    b= len(palabra2)
    if a > b:
        for indice in range(0, len(palabra1)):
            if palabra1[indice] not in palabra2 or palabra1.count(palabra1[indice]) > palabra2.count(palabra1[indice]):
                lista = list(palabra1)
                lista.remove(lista[indice])
                word = "".join(lista)
                if word == palabra2:
                    status = "IB"
                    break
    elif a < b:
        for indice in range(0, len(palabra2)):
            if palabra2[indice] not in palabra1 or palabra2.count(palabra2[indice]) > palabra1.count(palabra2[indice]):
                lista = list(palabra2)
                lista.remove(lista[indice])
                word = "".join(lista)
                if word == palabra1:
                    status = "IB"
                    break
    return status


def sustituir(palabra1, palabra2):
    status = "+1"
    for indice in range(0, len(palabra1)):
        if palabra1[indice] not in palabra2 :
            word1 = list(palabra1)
            word1.remove(word1[indice])
            word1.insert(indice, palabra2[indice])
            word = "".join(word1)
            if word == palabra2:
                status = "1S"
                break
    return status

if __name__=="__main__":
    pass
           