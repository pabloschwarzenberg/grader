#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    p1=list(palabra1)
    p2=list(palabra2)
    if p1==p2:
            return "0D"
    elif len(p1)>len(p2) or len(p1)<len(p2):
        if len(p1)+1==len(p2):
            contador=0
            p3=p1+p2
            for i in p3:
                l=p3.count(i)
                if l%2!=0:
                    contador=contador+1
                    l=p3.remove(i)
                elif l%2==0:
                    contador=contador
            if contador==1:
                return "IB"
            else:
                return "+1"
        elif len(p1)==len(p2)+1:
            contador=0
            p3=p1+p2
            for i in p3:
                l=p3.count(i)
                if l%2!=0:
                    contador=contador+1
                    l=p3.remove(i)
                elif l%2==0:
                    contador=contador
            if contador==1:
                return "IB"
            else:
                return "+1"
        else:
            return "+1"
    else: 
        contador=0
        p3=p1+p2
        for i in p3:
            l=p3.count(i)
            if l%2!=0:
                contador=contador+1
                l=p3.remove(i)
            elif l%2==0:
                contador=contador
        contador=contador-1
        if contador==1:
            return "1S"
        elif contador>1:
            return "+1"


if __name__=="__main__":
    palabra1=str(input("Ingrese su primera palabra: "))
    palabra2=str(input("Ingrese su segunda palabra: "))
    print(levenshtein(palabra1,palabra2))