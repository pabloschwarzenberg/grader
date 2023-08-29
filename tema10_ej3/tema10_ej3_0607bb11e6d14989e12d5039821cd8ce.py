def sopaletras(nombre_archivo,palabras):
    Sopa=[]
    Soluciones=[]
    archivo=open(nombre_archivo,"r")
    for linea in archivo.readlines():
        Linea=linea.split()
        Sopa.append(Linea)
        
    archivo.close()
    for palabra in palabras:
        for p in range(len(Sopa)):
         if palabra.upper()[0] in Sopa[p]:
             Pos=0
             k=0
             while Pos<len(Sopa)-1:
              Pos=Sopa[p].index(palabra.upper()[0],Pos+k)
              if Pos<len(Sopa[p])-1:
               if Sopa[p][Pos+1]==palabra.upper()[1]:
                 cd=1
                 for l in range(len(palabra)-2):
                     if Sopa[p][Pos+1+l]!=palabra.upper()[1+l]:
                         break
                     cd=cd+1   
                 if cd==len(palabra)-1:
                    Soluciones.append((palabra,[p,Pos],"derecha"))
                    break
                    break
              if p<len(Sopa)-1:
               if Sopa[p+1][Pos]==palabra.upper()[1]:
                 cd=1
                 for l in range(len(palabra)-2):
                     if Sopa[p+1+l][Pos]!=palabra.upper()[1+l]:
                         break
                     cd=cd+1
                 if cd==len(palabra)-1:
                     Soluciones.append((palabra,[p,Pos],"abajo"))
                     break
                     break
               if Sopa[p+1][Pos+1]==palabra.upper()[1]:
                 cd=1
                 for l in range(len(palabra)-2):
                     if Sopa[p+1+l][Pos+1+l]!=palabra.upper()[1+l]:
                         break
                     cd=cd+1
                 if cd==len(palabra)-1:
                     Soluciones.append((palabra,[p,Pos],"diagonal"))
                     break
                     break
              k=k+1
    return tuple(Soluciones) 
           