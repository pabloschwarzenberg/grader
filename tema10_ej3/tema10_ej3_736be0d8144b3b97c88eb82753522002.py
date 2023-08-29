def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras([(casa,[0,0],"derecha")]))
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt",["aro"]))
    print(sopaletras("sopa.txt",["casa","cra""aro"]))