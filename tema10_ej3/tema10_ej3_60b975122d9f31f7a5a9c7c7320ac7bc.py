def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["derecha"]))
    print(sopaletras("sopa.txt", ["diagonal"]))
    print(sopaletras("sopa.txt", ["abajo"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           