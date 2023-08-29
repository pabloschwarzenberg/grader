def Matriz_y_palabras(nombre_archivo, palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    datos=archivo.readlines()
    M,N=(datos[0].replace("\n","")).split(" ")
    matriz=[]
    for i in range (0,int(M)):
        columna=[]
        for j in range (0,int(N)):
            columna.append(datos[1+i][j])
            matriz.append(columna)
    palabras=datos[-1].split(",")
    return int(M),int(N),matriz,palabras

def verificando(op,i,j,matriz,palabra):
    if len(palabra)==1:
        respuesta=True	
        return respuesta
    else:
        if (op==1):
            i=i
            j=j+1
        elif (op==2):
            i=i
            j=j-1
        elif (op==3):
            i=i-1
            j=j
        elif (op==4):
            i=i-1
            j=j
        elif (op==5):
            i=i-1
            j=j-1
        elif (op==6):
            i=i+1
            j=j-1
        elif (op==7):
            i=i-1
            j=j+1
        elif (op==8):
            i=i+1
            j=j+1
        else:
            print ("ERROR [+]")
        try:
            if matriz[i][j]==palabra[0]:
                nueva=palabra[1:]
                a=verificando(op,i,j,matriz,nueva)
                if a==True:
                    return a
            else:
                respuesta=False
                return respuesta
        except:
            respuesta=False
            return respuesta

def Ocho_posibilidades(matriz,i,j,palabra):
    posibles={1:"hacia la derecha", 2:"hacia la izquierda", 3:"hacia arriba", 4:"hacia abajo", 5:"en forma Diagonal Superior Izquierda", 6:"en forma Diagonal Inferior Izquierda", 7:"en forma Diagonal Superior Derecha", 8:"en forma Diagonal Inferior Derecha"}
    nueva=palabra[1:]
    for x in range(1,9):
        veri=verificando(x,i,j,matriz,nueva)
        if (veri==True):
            print ("La palabra {0} esta ubicada en la posicion ({1},{2}) {3}").format(palabra,i+1,j+1,posibles[x])
            return veri
def Posicion_inicial(buscando,matriz,M,N):
    for i in range(0,M):
        for j in range(0,N):
            if (buscando[0] == matriz[i][j]):
                terminado=Ocho_posibilidades(matriz,i,j,buscando)
                if (terminado==True):
                    return terminado
M,N,matriz,palabras= Matriz_y_palabras()
for x in palabras:
    Posicion_inicial(x,M,N,Matriz)
