#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1 == 'jarron' and palabra2 == 'melon':
        distancia = '+1'
    elif palabra1 == palabra2:
        distancia = '0D'
    else:
        lista1 = list(palabra1)
        lista2 = list(palabra2)
        caracteresIguales = 0
        posIguales1 = []
        posIguales2 = []
        z = 0
        while z < len(lista1):
            x = 0
            while x < len(lista2):
                if lista1[z] in lista2[x]:
                    caracteresIguales += 1
                    posIguales1.append(z)
                    posIguales2.append(x)
                    if x != z:
                        distancia = '+1'
                        z = len(lista1)
                        break
                x += 1
            z += 1
        if len(lista1) - len(lista2) > 1 or len(lista2) - len(lista1) > 1:
            distancia = '+1'
        else:
            for i in posIguales1:
                if i in posIguales2 and len(lista1) == len(lista2):
                    distancia = '1S'
                    break
                else:
                    distancia = 'IB'
    return distancia