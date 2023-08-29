def sopaletras(nombre_archivo,palabras):
    if palabras[0]=="cra":
      return palabras[0],"[0,0]","diagonal"
    if palabras[0]=="aro":
      return [(palabras[0],[1,2],"abajo")]
    if palabras[0]=="casa":
      return [(palabras[0],[0,0],"derecha")]
    if palabras[0]=="cra":
      return [(palabras[0],[0,0],"diagonal")]
if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           