def sopaletras(nombre_archivo,palabras):
    sopa=[]
    archivo=open(nombre_archivo,"r")
    for line in archivo:
        linea=line.split()
        sopa.append(linea)
        archivo.close()
        sol=[]
    for palabra in palabras:
        palabritas=palabra.upper()
        k=""
        n_filas=len(sopa)
        n_columnas=len(sopa[0])
        lp=len(palabra)
        intento=0
        while intento<3:
         if n_columnas>=lp and intento==0:
             for i in range(0,(n_filas)):
               s=""
               t=0
               while t<=(n_columnas-lp):
                   for j in range(t,lp+t):
                       s+=sopa[i][j]
                       if s==palabritas:
                          k="derecha"
                          sol.append((palabra,[m,t],k))
                          t+=1
               intento=1
         elif n_filas>=lp and intento==1:
               for j in range(0,(n_columnas)):
                   s=""
                   t=0
                   while t<=(n_filas-lp):
                    for i in range(t,lp+t):
                      s+=sopa[i][j]
                      if s==palabritas:
                         sol.append((palabra,[t,j],k))
                         t+=1
               intento=2
         elif(n_filas**2+n_columnas**2)**(1/2)>=lp:
          s=""
          comienzo=[]
          for f in range(n_filas-1):
              for c in range(n_columnas-1):
                  a=(((c-n_columnas)**2+(f-n_filas)**2)**(1/2)-lp==(n_filas**2+n_columnas**2)**(1/2)-lp)
                  if a is True:
                     comienzo.append([f,c])
              for punto in comienzo:
                i=0
                while((punto[0]+i)**2+(punto[1]+i)**2)**(1/2)<=lp:
                   s+=sopa[punto[0]+i][punto[1]+i]
                   i+=1
                   if s==palabritas:
                    sol.append((palabra,punto,"diagonal"))
              intento = 3
        return sol
    return [(palabras[0],[0,0],"diagonal")]
if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           