#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
  if palabra1==palabra2:
    return "0D"
  palabra1=list(palabra1)
  palabra2=list(palabra2)
  contador=0
  s=0
  if len(palabra1)!=len(palabra2):
    if abs(len(palabra1)-len(palabra2))>1:
      return "+1"
    elif abs(len(palabra1)-len(palabra2))==1:
      if len(palabra1)<len(palabra2):
        palabra1.append("_")
        for i in range(0,len(palabra1)):
          if palabra1[i]!=palabra2[i] and s==0:
            palabra1.insert(i,palabra2[i])
            palabra1.remove("_")
            contador=contador+1
            s=s+1
          if palabra1[i]!=palabra2[i] and s==1:
            return "+1"
      elif len(palabra1)>len(palabra2):
        palabra2.append("_")
        for i in range(0,len(palabra2)):
          if palabra2[i]!=palabra1[i] and s==0:
            palabra2.insert(i,palabra1[i])
            palabra2.remove("_")
            contador=contador+1
            s=s+1
          if palabra2[i]!=palabra1[i] and s==1:
            return "+1"
      if contador==1:
        return "IB"
  if len(palabra1)==len(palabra2):
    for i in range(0,len(palabra1)):
        if palabra1[i]!=palabra2[i]:
          contador=contador+1
    if contador==1:
      return "1S"
    elif contador>1:
      return "+1"
  pass
if __name__=="__main__":
    pass
           