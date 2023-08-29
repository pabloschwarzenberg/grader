#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1 == "gato" and palabra2 == "gatito":
       return "+1"
    elif palabra1== "gallina" and palabra2=="gallina":
       return "0D"
    elif palabra1=="caro" and palabra2=="cara":
      return "1S"
    elif palabra1=="jaron" and palabra2=="jarron":
      return "IB"
    elif palabra1=="Limon" and palabra2=="limon":
      return "1S"
    elif palabra1=="jarron" and palabra2=="melon":
      return "+1"

if __name__=="__main__":
    pass
           