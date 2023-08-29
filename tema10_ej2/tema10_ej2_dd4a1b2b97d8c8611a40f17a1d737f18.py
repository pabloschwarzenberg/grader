#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1)==len(palabra2):
           i=0
           while i<len(palabra1) or i<len(palabra2):
                   if palabra1[i]!=palabra2[i]:
                          return "1S"
                          break
                   if palabra1[i]==palabra2[i]:
                          i=i+1
           return "0D"
    if len(palabra1)!=len(palabra2):
        if len(palabra1)>len(palabra2):
            for n in range(0,len(palabra2)):
                i=0
                if palabra1[n]!=palabra2[n]:
                    i=i+1
            x=len(palabra1)-len(palabra2)
            if i==1 and x==1:
                 return "+1"
            if i==1 and x==0:
                 return "IB"
            if i==1 and x==2:
                 return "+1"
            if i>2 and x>1:
                 return "+1"
            if i>2 and x>2:
                 return "+1"
    if len(palabra1)!=len(palabra2):
        if len(palabra2)>len(palabra1):
             for n in range(0,len(palabra1)):
                 i=0
                 if palabra1[n]!=palabra2[n]:
                     i=i+1
             x=len(palabra2)-len(palabra1)
             if i==1 and x==1:
                 return "IB"
             if i==1 and x==0:
                 return "IB"
             if i==2 and x==1:
                 return "+1"
             if i==1 and x==2:
                 return "+1"
             if i>2 and x==1:
                 return "+1"
             if i>2 and x>2:
                 return "+1"

if __name__=="__main__":
    pass
           