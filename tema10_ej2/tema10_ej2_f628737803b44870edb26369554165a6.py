#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):

    cont = 0
    for i in range(0,len(palabra1)):
        if palabra1[i] in palabra2:
            cont += 1
    
    salida = ""

    aux = cont
    cont = len(palabra1)-cont
    if aux > 1:
        salida = "+1"
    if ((len(palabra2)-1) == aux) or ((len(palabra2)+1) == aux):
        salida = "IB"
    if (len(palabra2)-1) == aux and cont == 1:
        salida = "1S"

    if palabra1 == palabra2:
        salida = "0D"
    return salida