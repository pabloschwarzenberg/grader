#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra,palabra2):
    if (palabra==palabra2):
        return "0D"
    n= len(palabra) 
    m =len(palabra2) 
    if n==0 and m>1:
        return "+1"
    if m==0 and n>1:
        return "+1"
    D=[[0 for j in range(m + 1)] for i in range(n + 1)]  
    for i in range(0, n + 1):
        D[i][0]=i
    for j in range(0, m + 1):
        D[0][j]=j 
    for i in range(1, n + 1): 
        s_i=palabra[i - 1] 
        for j in range(1, m + 1): 
            t_j = palabra2[j-1]
            if s_i==t_j :
                cost  = 0
            else:
                cost=1
            D[i][j]=min(D[i-1][j] +1,D[i][j-1]+1,D[i-1][j-1]+cost)
    if(D[n][m]>1):
        return "+1"
    if(D[n][m]==1):
        if (len(palabra)==len(palabra2)):
            return "1S"
    return "IB"


if __name__ == "__main__":
    pass
