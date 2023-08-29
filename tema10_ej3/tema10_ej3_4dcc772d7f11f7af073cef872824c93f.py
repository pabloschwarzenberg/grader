def verificando(op,i,j,matriz,palabra):
    if len(palabra) == 1: 
        return True
    else:
        if (op == 1): 
            j += 1
        elif (op == 2): 
            i += 1
        elif (op == 3): 
            i += 1
            j += 1
        else:
            print("ERROR [+]")
        try:
            if matriz[i][j].upper() == palabra[0].upper():
                nueva = palabra[1:] 
                resp = verificando(op,i,j,matriz,nueva)
                if resp:
                    return resp
                return False
        except:
            return False
            
def sopaletras(nombre_archivo, palabras):
    archivo=open(nombre_archivo,"r")
    lineas = archivo.readlines()
    matriz = []
    for linea in lineas:
      matriz.append(linea.split())
    archivo.close()
    respuesta = []

    for palabra in palabras:
        for i in range(0,len(matriz)):
            for j in range(0, len(matriz[0])):
                if(matriz[i][j].upper() == palabra[0].upper()):
                    direccion = {
                        1: "derecha",
                        2: "abajo",
                        3: "diagonal"
                    }
                    nueva = palabra[1:] 
                    for x in range(1,4): 
                        verificar=verificando(x,i,j,matriz,nueva)
                        if (verificar):
                            respuesta.append((palabra,[i,j],direccion[x]))
    return respuesta   

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           