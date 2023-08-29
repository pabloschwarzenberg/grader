#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass
    contador=0
    q=0
    b=list(palabra1)
    c=list(palabra2)
    if abs(len(b)-len(c))>1:
            print("+1")
    elif abs(len(b)-len(c))==1:
      print("IB")
    else:
        for i in range (0,len(b)):
            if b[i]==c[i] :
                i+=1
            elif b[i]!=c[i]:
                contador+=1
                i+=1
    if contador==1:
        if q==1:
            print("IB")
        else:
            print("1S")
    elif contador>1:
        print("+1")
    elif contador ==0:
        print("0D")

if __name__=="__main__":
    pass
           
 
 