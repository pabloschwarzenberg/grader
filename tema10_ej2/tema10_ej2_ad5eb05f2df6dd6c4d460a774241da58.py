#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    parte=""
    diferencia=0
    posicion=0
    lugar=palabra1
    if len(palabra1)!=len(palabra2):
        if ((len(palabra1)-len(palabra2))**2)==1:
            parte="IB"
            diferencia+=1
        else:
            parte="+1"
            posicion=len(palabra1)+8
            diferencia+=2
        if len(palabra1)<len(palabra2):
            lugar=palabra2
        while posicion<(len(lugar)/2):
            if palabra1[posicion]!=palabra2[posicion] and palabra1[-(posicion+1)]!=palabra2[-(posicion+1)]:
                diferencia+=1
            posicion+=1
        posicion+=len(lugar)+8
    else:
        while posicion<len(palabra1):
            if palabra1[posicion]!=palabra2[posicion]:
                diferencia+=1
            posicion+=1
    distancia=""
    if parte=="IB" and diferencia==1:
        distancia="IB"
    elif diferencia==1:
        distancia="1S"
    elif diferencia==0:
        distancia="0D"
    elif parte=="+1" or diferencia>1:
        distancia="+1"
    return distancia

if __name__=="__main__":
    palabra1=input("cual es la palabra: ")
    palabra2=input("cual es la otra palabra: ")
    distancia=levenshtein(palabra1,palabra2)
    print("la distancia es",distancia)

           