#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    x=palabra1
    y=palabra2
    contador=0
    if len(palabra1)>=len (palabra2):
        for i in palabra1:
            if i in palabra2:
                contador=contador
                palabra2=list(palabra2)
                palabra2.remove(i)
            else:
                contador+=1
    else:
        for i in palabra2:
            if i in palabra1:
                contador = contador
                palabra1 = list(palabra1)
                palabra1.remove(i)
            else:
                contador += 1
    if contador==0 and x==y:
        return "0D"
    elif contador>=2:
        return "+1"
    elif contador==1:
        if True:
            x=x.lower()
            a=len(x)
            y=y.lower()
            b=len(y)
            y=list(y)
            for i in x:
                if i in y:
                    y.remove(i)
                else:
                    continue
            if len(y)==0 or a==b:
                return "1S"
            else:
                return "IB"

if __name__=="__main__":
    a=levenshtein("jaron","jarron")
    print(a)