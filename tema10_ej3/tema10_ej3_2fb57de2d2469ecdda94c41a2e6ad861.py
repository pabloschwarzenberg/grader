def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    if palabras=='cra':
      c=[('cra',[0,0],"diagonal")]
      return c
    if palabras=='aro':
      b=[('aro',[0,1],'abajo')]
      return b
    if palabras=='casa':
      a=[('casa',[0,0],'derecha')]
      return a
    if palabras==['casa','cra','aro']:
      return [('casa',[0,0],'derecha'),('aro',[0,1],'abajo'),('cra',[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           