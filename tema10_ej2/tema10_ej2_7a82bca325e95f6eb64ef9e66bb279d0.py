#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  contador = 0
  if len(palabra1) - len(palabra2) > 1 or len(palabra2) - len(palabra1) >1:
    h = "+1"
    return h
  for f in palabra1:
    if f not in palabra2:
      contador = contador + 1
      print(contador)
    elif contador > 1:
      h = "+1"
      return h      
  else:
    if palabra1 == palabra2:
      h = "0D"
    elif len(palabra1)==len(palabra2):
      h = "1S"
    else:
      h = "IB"    
  return h

  pass

if __name__=="__main__":
  palabra1 = input()
  palabra2 = input()
  print(levenshtein(palabra1,palabra2))
  pass