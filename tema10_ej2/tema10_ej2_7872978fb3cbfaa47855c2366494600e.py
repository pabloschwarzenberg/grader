#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    palabra1 = ' '+palabra1
    palabra2 = ' '+palabra2

    size1 = len(palabra1)
    size2 = len(palabra2)

    lista = {}
    
    for a in range(size1):
        lista[a,0] = a

    for b in range(size2):
        lista[0,b]= b

    for x in range(1,size2):
        
        for y in range(1,size1):

            if palabra1[y] == palabra2[x]:
                lista[y,x] = lista[y-1,x-1]
            else:
                lista[y,x] = min(lista[y-1,x], lista[y,x-1],lista[y-1,x-1])+1

    levenshtein = lista[size1-1,size2-1]
    mensaje = ''

    if levenshtein == 0:
        mensaje = '0D'
    if levenshtein == 1:
        if size1 == size2:
            mensaje = '1S'
        if size1 != size2:
            mensaje = 'IB'

    if levenshtein > 1:
        mensaje = '+1'

    return mensaje