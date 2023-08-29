#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    distancia = 0
    if len(palabra1) > len(palabra2):
        minimo = palabra2
        maximo = palabra1
    else:
        minimo = palabra1
        maximo = palabra2
    for i in maximo:
        iguales = 0
        distintos = iguales
        for j in minimo:
            if i == j:
                distintos += 1
                letra = j
                minimo = minimo.replace(letra, " ", 1)
                break
        print(minimo)
        if distintos == iguales:
            distancia += 1
    if distancia == 0:
        valor = "0D"
    elif distancia == 1 and len(palabra2) == len(palabra1):
        valor = "1S"
    elif distancia == 1:
        valor = "IB"
    elif distancia > 1:
        valor = "+1"
    return valor

if __name__=="__main__":
    x = input()
    y = input()
    print(levenshtein(x,y))