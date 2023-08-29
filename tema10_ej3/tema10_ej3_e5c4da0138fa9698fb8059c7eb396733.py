def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    sopa = []
    for linea in archivo:
      lista = linea.lower().strip("\n").split()
      sopa.append(lista)
    archivo.close()
    res = []
    for pal in palabras:
      for i in range(len(sopa)):
        for j in range(len(sopa[0])):
          rev = ""
          for k in range(j,len(sopa[0])):
              if k < len (sopa[0]):
                rev+=sopa[i][k]
          if rev==pal:      
           res.append((pal,[i,j],"derecha"))
      for i in range(len(sopa)):
        for j in range(len(sopa[0])):
            rev = ""
            for k in range(i,len(sopa)):
              if k<len(sopa):
                 rev+=sopa[k][j]
            if rev == pal:
                res.append((pal,[i,j],"abajo"))
      for i in range(len(sopa)):
        for j in range(len(sopa[0])):
            rev = ""
            m = i
            for k in range(j,len(sopa[0])):
              if m<len(sopa) and m <len(pal):
                 rev+=sopa[m][k]
                 m+=1
            if rev == pal:
                res.append((pal,[i,j],"diagonal"))
    return res

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
