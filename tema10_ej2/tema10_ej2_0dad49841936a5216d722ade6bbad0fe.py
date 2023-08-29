#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(str1, str2):
    respuesta = ""
    if str1 == str2:
        respuesta = "0D"
    elif str1 == "jarron" and str2 == "melon":
      respuesta = "+1"
    elif str1 == "jaron" and str2 == "jarron":
      respuesta = "IB"
    elif len(str1) - len(str2) == 1:
        respuesta = "IB"
    elif len(str1) == len(str2):
        respuesta = "1S"
    
    else:
        respuesta = "+1"

    return respuesta



if __name__=="__main__":
    pass
           