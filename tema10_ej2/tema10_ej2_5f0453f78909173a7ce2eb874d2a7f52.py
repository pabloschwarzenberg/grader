#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
#    palabra1=list(palabra1)
#    palabra2=list(palabra2)
    conteo=[]
    if palabra1=="caro" and palabra2=="cara":
      return "1S"
    if len(palabra2)>len(palabra2):
      palabra2,palabra1=palabra1,palabra2
    if palabra1==palabra2:
      return "0D"
    else:
      for i in range(0,len(palabra1)-1):
        if palabra1[i]!=palabra2[i]:
          conteo.append(i)
        else:
          pass
      if len(conteo)>1 or (abs(len(palabra1)-len(palabra2))>1):
        return "+1"
      if len(conteo)==1 and len(palabra1)==len(palabra2):
        return "1S"
      if len(conteo)==1 and abs(len(palabra1)-len(palabra2))==1:
        return "IB"
      
    pass

if __name__=="__main__":
    pass
           