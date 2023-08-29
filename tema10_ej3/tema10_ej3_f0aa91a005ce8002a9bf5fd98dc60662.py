def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    
    print("sopa.txt",["cra"])
    print("sopa.txt", ["aro"])
    print("sopa.txt", ["casa"])
    print("sopa.txt",["casa","cra","aro"])

           