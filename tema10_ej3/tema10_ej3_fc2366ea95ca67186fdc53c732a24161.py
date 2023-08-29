def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    ((archivo.close())
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cara"]))
    print(sopaletras("sopa.txt", ["caro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cara","caro"]))

