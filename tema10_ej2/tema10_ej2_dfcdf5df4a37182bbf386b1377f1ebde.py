#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  if palabra1==palabra2:
    return 'OD'
  elif len(palabra1) == len(palabra2):
    n_reemplazar = 0
      for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
          n_reemplazar += 1
        if n_reemplazar > 1:
          return '+1'
       else:
         return '1S'
  elif abs(len(palabra1) - len(palabra2)) == 1:
    if len(palabra1) > len(palabra2):
    # remover
      for i in range(len(palabra1)):
        if palabra1[:i] + palabra1[i+1:] == palabra2:
          return 'IB'
      return '1+'
  else:
  # agregar
    for i in range(len(palabra2)):
      if palabra2[:i] + palabra2[i+1:] == palabra1:
        return 'IB'
    return '+1'
      else:
        return '+1'

if __name__=="__main__":
    pass
           