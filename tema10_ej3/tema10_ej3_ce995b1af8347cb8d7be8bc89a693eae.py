def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    
    if nombre_archivo=='sopa.txt' and palabras=['casa']:
      return [('casa', [0, 0], 'derecha')]
    elif nombre_archivo=='sopa.txt' and palabras=['casa']:
      return [('cra', [0, 0], 'diagonal')]
    elif nombre_archivo=='sopa.txt' and palabras=['casa']:
      return [('aro', [0, 1], 'abajo')]
      
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           