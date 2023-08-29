#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son igua
def levenshtein(palabra1,palabra2):
    a=0
    P1=list(palabra1)
    P2=list(palabra2)
    if len(palabra1)<=len(palabra2):
      x=P1
      y=P2
    elif len(palabra1)>len(palabra2):
      x=P2
      y=P1
    if len(x)==len(y):
      for i in x:
        if not i in y:
          a+=1
        else:
          pass
    if len(x)!=len(y):
      a+=(len(y)-len(x))
      for i in x:
        if not i in y:
          a+=1
        else:
          pass
    if a>1:
      return "+1"
    if a==1:
      if len(y)==len(x):
        return "1S"
      else:
        return "IB"
    if a==0:
      return "0D"
      
    


        


           