#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    n = len(palabra1)
    m = len(palabra2)
    distancia = []
    for i in range(n+1):
        fila = []
        for j in range(m+1):
            if i == 0:
                fila.append(j)
            elif j == 0:
                fila.append(i)
            else:
                fila.append(0)
        distancia.append(fila)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if palabra1[i-1] == palabra2[j-1]:
                distancia[i][j] = distancia[i-1][j-1]
            else:
                distancia[i][j] = 1 + min(distancia[i][j-1], distancia[i-1][j], distancia[i-1][j-1])

    d = distancia[n][m]
    if d > 1:
        return "+1"
    elif d == 1:
        if n > m:
            return "IB"
        elif n < m:
            return "IB"
        else:
            return "1S"
    else:
        return "0D"
    
   

if __name__=="__main__":
    print(levenshtein("gato", "gatito")) # +1
    print(levenshtein("hola", "ola")) # IB
    print(levenshtein("gallina", "gallina")) # 0D
    print(levenshtein("caro", "cara")) # 1S
    pass
           