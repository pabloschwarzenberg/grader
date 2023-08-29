#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    z = len(palabra1)
    x = len(palabra2)
    tabla=[]
    for i in range(z+1):
        tabla.append([])
        for l in range(x+1):
            tabla[i].append("0")
    for i in range(z+1):
        tabla[i][0] = i
    for j in range(x+1):
        tabla[0][j] = j
    for i in range(1, z+1):
        for j in range(1,x+1):
            if palabra1[i-1] == palabra2[j-1]:
                tabla[i][j] = tabla[i-1][j-1]
            else:
                borrar=tabla[i-1][j]
                insertar=tabla[i][j-1]
                sustituir=tabla[i-1][j-1]
                tabla[i][j] = 1 + min(borrar,insertar,sustituir)
    if tabla[-1][-1] == 0:
        return("0D")
    if tabla[-1][-1] > 1:
        return("+1")
    if tabla[-1][-1] == 1:
        a1=z
        a2=x
        i=tabla[a1-1][a2]
        d=tabla[a1][a2-1]
        s=tabla[a1-1][a2-1]
        dt=min(d,i,s)
        a3=min(d,i,s)
        while a3 == 1:
            i=tabla[a1-1][a2]
            d=tabla[a1][a2-1]
            s=tabla[a1-1][a2-1]
            dt=min(d,i,s)
            if dt == d:
                a1-=1
                a3=tabla[a1-1][a2]
            elif dt == i:
                a2-=1
                a3=tabla[a1][a2-1]
            elif dt == s:
                a1-=1
                a2-=1
                a3=tabla[a1-1][a2-1]
        if dt == d:
            return("IB")
        elif dt == i:
            return("IB")
        elif dt == s:
            return("1S")
if __name__=="__main__":
    pass
           