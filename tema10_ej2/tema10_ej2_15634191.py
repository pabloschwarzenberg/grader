#La funcion debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pal1=[]
    pal2=[]
    for i in palabra1:
        pal1.append(i)
        palabra1.lstrip(i)
    for i in palabra2:
        pal2.append(i)
        palabra2.lstrip(i)
    print(pal1,pal2)
    max=palabra1
    min=palabra2
    if len(pal2)>len(pal1):
        max=palabra2
        min=palabra1
    if len(max)==len(min):
        cont=0
        for i in pal1:
            if pal2[pal1.index(i)]!=i:
                cont+=1
        if cont==1:
            return "1S"
        if cont==0:
            return "0D"

    if len(max)-len(min)==1:
        for i in max:
            if i in pal1 and i in pal2:
                pal1.remove(i)
                pal2.remove(i)
        if pal1==[] or pal2==[]:
            return "IB"
        else:
            return "+1"
    else:
        return "+1"