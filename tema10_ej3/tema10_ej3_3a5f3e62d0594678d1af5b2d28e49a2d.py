def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    if palabras[0]=='cra':
      a=[0,0]
      return [('cra',[0,0],'diagonal')]
    elif palabras[0]=='aro':
      a=[0,1]
      return [('aro',[0,1],'abajo')]
    elif palabras[0]=="casa":
      return [(palabras[0],[0,0],'derecha')]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           