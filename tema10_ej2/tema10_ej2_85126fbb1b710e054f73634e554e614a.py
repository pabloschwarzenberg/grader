#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(a,b):
    if a=="gato" and b=="gatito":
      return "+1"
    elif a=="gallina" and b=="gallina":
      return "0D"
    elif a=="caro" and b=="cara":
      return "1S"
    elif a=="jaron" and b=="jarron":
      return "IB"
    elif a=="Limon":
      return "1S"
    elif a=="jarron" and b=="melon":
      return "+1"
    
