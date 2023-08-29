def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           def buscarTodas(a,b):
          m=[i for i,x in enumerate(a) if x==b]
          z=list(m)
          l=[]
          for i in z:
                    l.append(str(i))
          w=" ".join(l)
          return w