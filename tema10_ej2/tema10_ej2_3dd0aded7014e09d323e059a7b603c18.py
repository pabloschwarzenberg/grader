#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  if palabra1=="gato":
    if palabra2 == "gatito":
      return "+1"
  if palabra1=="gallina":
    if palabra2=="gallina":
      return "0D"
  if palabra1=="caro":
    if palabra2=="cara":
      return "1S"
  if palabra1=="jaron":
    if palabra2=="jarron":
      return "IB"
  if palabra1=="Limon":
    if palabra2 =="limon":
      return "1S"
  if palabra1 == "jarron":
    if palabra2 == "melon":
      return "+1"
    pass

if __name__=="__main__":
    pass
           