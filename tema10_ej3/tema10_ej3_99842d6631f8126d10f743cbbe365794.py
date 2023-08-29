def Sopadeletras(N):
    sopa =[]
    for i in range(N):
        sopa.append([])
        for j in range(N):
            sopa[i].append(" ")
            sopa[i][j]=alfabeto[random.randint(0, 25)]
    return sopa

def de_izquierda_a_derecha(sopa,palabra):
    for i in range(len(palabra)):
        sopa[N-1][i]= palabra[ i ]
    return sopa

def de_derecha_a_izquierda(sopa, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        sopa[N-3][i-len(palabra)]=palabra[i]
    return sopa

def de_arriba_abajo(sopa,palabra):
    for i in range(len(palabra)):
        sopa[i][N-1]= palabra[ i ]
    return sopa

def de_abajo_arriba(sopa, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        sopa[i-len(palabra)][N-3]=palabra[i]
    return sopa

def diagonal_de_arriba_abajo(sopa, palabra):
    for i in range(len(palabra)):
        sopa[i][i]= palabra[ i ]
    return sopa

def diagonal_de_abajo_arriba(sopa, palabra):
    palabra=palabra[::-1]
    for i in range(len(palabra)):
        sopa[i-len(palabra)][i]= palabra[ i ]
    return sopa   


if __name__=="__main__":
    N=int(input())
    numero_de_palabras=int(input())
    for i in range(numero_de_palabras):
        lista_palabras=[]
        palabras=input()
        lista_palabras.append(palabras)
        if len(palabras)>N:
             print("la palabra no se puede incluir en la sopa de letras")
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           