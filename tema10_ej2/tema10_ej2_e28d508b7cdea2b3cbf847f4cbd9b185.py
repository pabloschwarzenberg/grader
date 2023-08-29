#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  PALABRA1=list(palabra1)
  PALABRA2=list(palabra2)
  levesn=0
  for p in PALABRA1:
    for l in PALABRA2:
        if len(PALABRA1) == len(PALABRA2):
            if p!=l:
                levesn=1
            elif p==l:
                levesn=0
        elif len(PALABRA1) >= len(PALABRA2) or len(PALABRA1)<= len(PALABRA2):
            if l not in PALABRA1 or p not in PALABRA2:
                levesn+=2
  if levesn==1:
      return "1S"
  elif levesn==2:
      return "IB"
  elif levesn==0:
    return "0D"
           