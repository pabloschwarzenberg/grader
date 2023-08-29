#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    palabra1=list(palabra1)
    palabra2=list(palabra2)
    copiaPalabra = list(palabra1)
    for i in range(len(palabra1)):
      if palabra1[i] in palabra2:
        palabra2.remove(palabra1[i])
        copiaPalabra.remove(palabra1[i])
    if len(palabra2) > 1:
      return "+1"
    elif len(copiaPalabra) == 0 and len(palabra2) == 1:
      return "IB"
    elif len(copiaPalabra) == 1 and len(palabra2) == 1:
      return "1S"
    else:
      return "0D"

if __name__=="__main__":
    pass
           