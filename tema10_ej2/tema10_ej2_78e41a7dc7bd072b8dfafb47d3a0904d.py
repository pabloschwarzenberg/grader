"""La función debe retornar la distancia como un string:
+1 : si la distancia es mayor que 1
IB : si la distancia es 1, y para llegar de una palabra a la otra hay que insertar o borrar una letra
1S : si la distancia es 1 porque hay que sustituir una letra
0D : si las palabras son iguales"""
def levenshtein(a, b):

    largo_a = len(a)
    largo_b = len(b)
    matriz = [[0] * (largo_b + 1) for _ in range(largo_a + 1)]

    for i in range(largo_a + 1):
        matriz[i][0] = i
    for j in range(largo_b + 1):
        matriz[0][j] = j

    for i in range(1, largo_a + 1):
        for j in range(1, largo_b + 1):
            if a[i - 1] == b[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = 1 + min(matriz[i - 1][j], matriz[i][j - 1], matriz[i - 1][j - 1])

    if matriz[-1][-1] > 1 :
        return "+1"
    elif matriz[-1][-1] == 1 :
        if largo_a == largo_b or a == b:
            return "1S"
        else:
            return "IB"
    elif matriz[-1][-1] == 0:
        return "0D"

if __name__=="__main__":
    str1=input("Ingrese la primera oracion: ")
    str2=input("Ingrese la segunda oracion: ")
    print(levenshtein(str1,str2))