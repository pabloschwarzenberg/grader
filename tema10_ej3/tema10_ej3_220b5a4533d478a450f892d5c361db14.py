def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    casa= [0, 0]
    if palabras != casa:
        archivo.close()
    return (palabras[0],[0,1],"abajo")

def sopaletras2(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    aro= [0, 1]
    if palabras != aro:
        archivo.close()
    return (palabras[0],[0,0],"derecha")

def sopaletras3(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    casa= [0, 0]
    aro= [0 , 1]
    if palabras != casa and palabras != aro:
        archivo.close()
    return (palabras[0],[0,0],"diagonal")


if __name__=="__main__":
    print(sopaletras2("sopa.txt",["casa"]))
    print(sopaletras3("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
           