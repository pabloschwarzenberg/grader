def CrearMatrizA (m, n):
    return [[0.0 for j in range (n)] for i in range (m)]
def CrearMatrizB (m, n):
    return [[0.0 for k in range (n)] for p in range (m)]
def CrearMatrizC (m, n):
    return [[0.0 for x in range (n)] for y in range (m)]

def EntrarDatos (matriz):
    m = len(matriz)
    n = len(matriz[0])
    for i in range(m):
        for j in range (n):
            matriz [i] [j] = float(input( "m["+ str(i) + "][" + str(j) + "]?"))
    return

def EntrarDatosC (matriz):
    m = len(A)
    n = len (B[0])
    for x in range (m):
        for y in range (n):
            matriz [x][y] = MultiplicarMatriz (A, B, C)
    return

def MostrarMatriz(matriz):
    m = len(matriz)
    n = len(matriz[0])
    for i in range (m):
        for j in range (n):
            print (matriz [i][j])
        print
    return


def MultiplicarMatriz(A, B, C):
    m1 = len(A)
    n1 = len(A[0])
    m2 = len(B)
    n1 = len(B[0])
    x = 0
    y = 0
    for p in range (m2):
        for i in range (m1):
            for j in range (n1): 
                for k in range (m2):
                    l = A[i][j] * B[k][p]
                    C[x][y] = C[x][y] + l
                    j = j + 1
                    k = k + 1
        i = i + 1
        x = x + 1
        j = 1
        k = 1
    p = p + 1
    y = y + 1
    x = 1
    i = 1
    return 


def main():
    m1 = int(input("Digite la cantidad de filas de la primera matriz: "))
    n1 = int(input("Digite la cantidad de columnas de la primera matriz: "))
    m2 = int(input("Digite la cantidad de filas de la segunda matriz: "))
    n2 = int(input("Digite la cantidad de columnas de la segunda matriz: "))

    if((m1, m2, n1, n2 > 0) and (m1 == n2)):
        '''hay un problema cuando todos son cero'''
        A = CrearMatrizA(m1, n1)
        EntrarDatos(A)
        B = CrearMatrizB(m2, n2)
        EntrarDatos (B)
        C = CrearMatrizC(m1, n2)
        C = MultiplicarMatriz(A, B, C)

        MostrarMatriz(A)
        MostrarMatriz(B)
        MostrarMatriz (C)   
    else:
       print("Las matrices no son multiplicables")    
    return