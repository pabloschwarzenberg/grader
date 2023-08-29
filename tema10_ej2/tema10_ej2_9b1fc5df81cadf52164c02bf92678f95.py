#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  if palabra1==palabra2:
    return '0D'
  else:
    p1 = list(palabra1)
    p2 = list(palabra2)
    if len(palabra1)==len(palabra2): 
      d = 0
      for a in range(len(palabra1)):
        if p1[a]!=p2[a]:
          d += 1
      if d==1:
        return '1S'
      elif d>1:
        return '+1'     
    elif len(palabra1)!=len(palabra2):
      i = 0
      j = 0
      if len(palabra1)<len(palabra2):
        h = 0
        while j<len(palabra2) and i<len(palabra1):
          if p1[i]==p2[j]:
            i += 1
            j += 1
          else:
            j += 1
            h += 1
        if h==1:
          return 'IB'
        elif h>1:
          return '+1'
      elif len(palabra1)>len(palabra2):
        h = 0
        while j<len(palabra2) and i<len(palabra1):
          if p1[i]==p2[j]:
            i += 1
            j += 1
          else:
            i += 1
            h += 1
        if h==1:
          return 'IB'
        elif h>1:
          return '+1'

if __name__=="__main__":
    palabra1 = 'gato'
    palabra2 = 'gatito'
    print(levenshtein(palabra1,palabra2))
           