def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    filas=[list(archivo.readline()),list(archivo.readline()),list(archivo.readline())]
    archivo.close()
    
    I1=[filas[0][0],filas[0][2],filas[0][4],filas[0][6]]
    I2=[filas[1][0],filas[1][2],filas[1][4],filas[1][6]]
    I3=[filas[2][0],filas[2][2],filas[2][4],filas[2][6]]
    A1=filas[0][0]+filas[1][0]+filas[2][0]+filas[3][0]
    A2=filas[0][1]+filas[1][1]+filas[2][1]+filas[3][1]
    A3=filas[0][2]+filas[1][2]+filas[2][2]+filas[3][2]
    A4=filas[0][3]+filas[1][3]+filas[2][3]+filas[3][3]
    D1=0
    D2=0
    
    

    
    return F1,F2,F3
    #return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))


           