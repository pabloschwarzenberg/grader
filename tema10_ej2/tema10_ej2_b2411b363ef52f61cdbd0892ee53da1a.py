#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    l=[]
    m=[]
    if len(palabra1)<len(palabra2):
      for i in range(0,len(palabra1))
        if palabra1[i]!=palabra2[i]:
          l.append(i)
      for i in range(0,len(palabra2)):
        if palabra1[i]!=palabra2[i]:
          l.append(i)
    else:
      pass
    dist=len(l)+abs(len(palabra1)-len(palabra2))    
    
  print(dist)
           