#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    d=abs(len(palabra2)-len(palabra1))
    if d>1:
        distancia='+1'
    elif d==1:
        palabra1=palabra1+'*'
        for i in range(len(palabra2)):
            if palabra1[i]!=palabra2[i]:
                d=d+1
            else: 
                d=d-1
     
        if d>2:
          distancia='+1'
        else:
          distancia='IB'
      
    elif d==0:
        for i in range(len(palabra1)):
            if palabra1[i]!=palabra2[i]:
                d=d+1
        if d>1:
          distancia='+1'
        elif d==1:
          distancia='1S'
        else:
          distancia='0D'
    return distancia
