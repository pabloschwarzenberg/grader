#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
      return "0D"
    elif len(palabra1)==len(palabra2):
      return "1S"
    elif len(palabra1)-len(palabra2)<=-2 or len(palabra1)-len(palabra2)>=2:
      return "+1"
    counter=0
    if len(palabra1)<len(palabra2):
      for i in list(palabra1):
            if palabra1.count(i)!=palabra2.count(i):
              counter=counter+1
      if counter==1:
        return "IB"
      if counter>1:
        return "+1"
    counter=0
    if len(palabra1)>len(palabra2):
      for i in list(palabra2):
            if palabra2.count(i)!=palabra1.count(i):
              counter=counter+1
      if counter==1:
        return "IB"
      if counter>1:
        return "+1"

if __name__=="__main__":
    pass
           