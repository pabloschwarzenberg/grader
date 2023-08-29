import random 


alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def crear_matrix(N):
    matrix =[]
    for i in range(N):
        matrix.append([])
        for j in range(N):
            matrix[i].append(" ")
            matrix[i][j]=alfabeto[random.randint(0, 25)]
    return matrix

def de_izquierda_a_derecha(matrix,palabra):
    for i in range(len(palabra)):
        matrix[N-1][i]= palabra[ i ]
    return matrix

def de_derecha_a_izquierda(matrix, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        matrix[N-3][i-len(palabra)]=palabra[i]
    return matrix

def de_arriba_abajo(matrix,palabra):
    for i in range(len(palabra)):
        matrix[i][N-1]= palabra[ i ]
    return matrix

def de_abajo_arriba(matrix, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        matrix[i-len(palabra)][N-3]=palabra[i]
    return matrix

def diagonal_de_arriba_abajo(matrix, palabra):
    for i in range(len(palabra)):
        matrix[i][i]= palabra[ i ]
    return matrix

def diagonal_de_abajo_arriba(matrix, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        matrix[i-len(palabra)][i]= palabra[ i ]
    return matrix   


numero_de_palabras=int(input())
for i in range(numero_de_palabras):
    lista_palabras=[]
    palabras=input()
    lista_palabras.append(palabras)
    if len(palabras)>N:
        print("la palabra no se puede incluir en la sopa de letras")
    print(lista_palabras)
    
   
           