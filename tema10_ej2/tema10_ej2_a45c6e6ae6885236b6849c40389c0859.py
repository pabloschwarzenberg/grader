#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def funcion_levenshtein(palabra_1,palabra_2):
    lista_palabra_1 = list(palabra_1)
    lista_palabra_2 = list(palabra_2)
    letra = 0
    while letra < len(lista_palabra_1):
        
        i = 0
        while i < len(lista_palabra_2):
            if (len(lista_palabra_1) > 0) and (len(lista_palabra_2) > 0):
                if  lista_palabra_1[letra] == lista_palabra_2[i]:
                    lista_palabra_1.pop(letra)
                    lista_palabra_2.pop(i)

                    i = i - 1
            i = i + 1
            
        letra = letra + 1

    if len(lista_palabra_1) > len(lista_palabra_2):
        if len(lista_palabra_1) > 1:
            #el largo L es mayor a 1
            return "+1"
        elif len(lista_palabra_1) == 1:
            #el largo L es 1
            return "IB"

    elif len(lista_palabra_1) < len(lista_palabra_2):
        if len(lista_palabra_2) > 1:
            #el largo L es mayor a 1
            return "+1"
        elif len(lista_palabra_2) == 1:
            #el largo L es 1
            return "IB"
    elif (len(lista_palabra_1) == len(lista_palabra_2)) and (len(lista_palabra_1) > 0):
        #el largo L es de sustituir
        return "1S"
    
    elif (len(lista_palabra_1) == len(lista_palabra_2)) and (len(lista_palabra_1) == 0):
        #el largo L es de sustituir
        return "0D"
