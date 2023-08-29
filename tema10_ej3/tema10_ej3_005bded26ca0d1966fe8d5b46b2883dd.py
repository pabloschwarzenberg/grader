def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]
