def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    palabras= list(palabras)
    palabras_separadas= []
    for palabra in palabras:
        lista_palabra= list(palabra)
        palabras_separadas.append(lista_palabra)
    for linea in archivo:
        linea= linea.split()
        
        
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           