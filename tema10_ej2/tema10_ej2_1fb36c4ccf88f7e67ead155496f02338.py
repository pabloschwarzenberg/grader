#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales


def lev(s1, s2, a, b):
  c = 0
  if a ==0:
    return b
  elif b == 0:
    return a
  if s1[a-1] == s2[b-1]:
    c = 0
  else:
    c = 1
  p = lev(s1, s2, a-1 ,b) + 1
  q = lev(s1, s2, a, b-1) + 1
  r = lev(s1, s2, a-1, b-1) + c
  
  return min(p, q, r)



def levenshtein(palabra1, palabra2):
    a = len(palabra1)
    b = len(palabra2)
    levy = lev(palabra1, palabra2, a, b)
    if levy > 1:
        return "+1"
    elif levy == 1 and a != b:
        return "IB"
    elif levy == 1 and a == b:
        return "1S"
    elif palabra1 == palabra2:
        return "0D"

if __name__=="__main__":
    pass
           