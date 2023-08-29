def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    L=[]
    for line in archivo:
      l=line.split()
      L.append(l)
    archivo.close()
    for i in range(len(L)):
        l="".join(L[i])        
        k=l.find(palabras[0])
        if k!=-1:
            return "{},[{},{}],{}".format(palabras[0],k,i,"derecha")
    M=[]
    for i in range(len(L[0])):
      m=""
      for j in L:
        m+=j[i]
      M.append(m)
    for i in range(len(M)):
          k=M[i].find(palabras[0])
          if k!=-1:
            return "{},[{},{}],{}".format(palabras[0],i,k,"abajo")
    s=""
    for i in range(min(len(L),len(L[0]))):
      s+=str(L[i][i])
    M=[s]
    for i in range(1,len(L[0])):
      m=""
      n=""
      for j in range(len(L)):
        if j+i<len(L) and j<len(L[0]):
          m+=L[j+i][j]
        if j<len(L) and j+i<len(L[0]):
          n+=L[j][j+i]
      if n!="":
          M.append(n)
      if m!="":
          M.append(m)
    print(M)
    for o in range(len(M)):
      k=M[o].find(palabras[0])
      if k!=-1:
        print(k,o)
        if o%2==0:
          a=k
          b=k+(o+1)//2
        else:
          a=k+(o+1)//2
          b=k
        return "{},[{},{}],{}".format(palabras[0],a,b,"diagonal")
        
  
if __name__=="__main__":
    pass

           