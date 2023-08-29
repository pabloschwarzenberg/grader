import random 
abecedario =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
palabra = ["casa", "cra", "aro"]
def crear_juego(N):
    juego =[]
    for i in range(N):
        juego.append([])
        for j in range(N):
            juego[i].append(" ")
            juego[i][j]=abecedario[random.randint(0, 25)]
    return juego
def dizquierda_derecha(juego,palabra):
    for i in range(len(palabra)):
        juego[N-1][i]= palabra[ i ]
    return juego

def dderecha_izquierda(juego, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        juego[N-3][i-len(palabra)]=palabra[i]
    return juego

def arriba_abajo(juego,palabra):
    for i in range(len(palabra)):
        juego[i][N-1]= palabra[ i ]
    return juego

def dabajo_arriba(juego, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        juego[i-len(palabra)][N-3]=palabra[i]
    return juego

def diagonal_arriba_abajo(juego, palabra):
    for i in range(len(palabra)):
        juego[i][i]= palabra[ i ]
    return juego

def diagonal_de_abajo_arriba(juego, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        juego[i-len(palabra)][i]= palabra[ i ]
    return juego   

           