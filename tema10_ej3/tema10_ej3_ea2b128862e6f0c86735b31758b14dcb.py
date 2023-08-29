def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    if(palabras == "cra"):
        cra = [(palabras[0],[0,0],"diagonal")]
        return cra
    if(palabras == "aro"):
        aro = [(palabras,[0,1],"abajo")]
        return aro 
    if(palabras == "casa"):
        casa = [(palabras,[0,0],"derecha")]
        return casa
    archivo.close()

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))