#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  if palabra1 == palabra2:
    return "0D"
  elif len(palabra1) == len(palabra2) and palabra1 != palabra2:
    return "1S"
  # elif (abs(len(palabra1) - len(palabra2))) == 1:
  #   return "IB"
  else:
    dist = abs(len(palabra1) - len(palabra2))
    if (abs(len(palabra1) - len(palabra2))) == 1:
      if len(palabra1) < len(palabra2):
        for i in range(len(palabra1)):
          if palabra1[i] != palabra2[i] and palabra1[i] != palabra2[i+1]:
            dist += 1
      elif len(palabra1) > len(palabra2):
        for i in range(len(palabra2)):
          if palabra1[i] != palabra2[i] and palabra2[i] != palabra1[i+1]:
            dist += 1 
    else:  
      if len(palabra1) < len(palabra2):
        for i in range(len(palabra1)):
          if palabra1[i] != palabra2[i]:
            dist += 1
      elif len(palabra1) > len(palabra2):
        for i in range(len(palabra2)):
          if palabra1[i] != palabra2[i]:
            dist += 1
    if dist > 1:
      return "+1"
    elif dist == 1:
      return "IB"