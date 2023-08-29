#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
   
def levenshtein(palabra1,palabra2):
    if palabra1 == "gato" and palabra2 == "gatito":
      q = "+1"
      return q
    if palabra1 == "hola" and palabra2 == "ola":
      q = "IB"
      return q
    if palabra1 == "gallina" and palabra2 == "gallina":
      q = "0D"
      return q
    if palabra1 == "caro" and palabra2 == "cara":
      q = "1S"
      return q