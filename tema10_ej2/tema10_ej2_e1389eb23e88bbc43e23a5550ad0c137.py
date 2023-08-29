#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
if __name__=="__main__":
  palabra1=input("Inserte la primera palabra:")
  palabra2=input("Inserte la segunda palabra:")
  def levenshtein(palabra1,palabra2):
    if distancia >1:
      return "+1"
    if distancia ==1 and palabra1 +- 1 letra=palabra2:
      return "IB"
    if distancia==1 and palabra1 +sustitucion=palabra2:
      return "1S"
    if palabra1==palabra2:
      return "0D"
           