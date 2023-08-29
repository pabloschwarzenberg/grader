def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    string = archivo.read()
    archivo.close()
    
    print(string)
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           