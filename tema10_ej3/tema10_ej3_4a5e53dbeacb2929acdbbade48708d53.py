def archivo_matriz(fail):
    archivo=open(fail,"r")
    lista=archivo.readlines()
    lista=list(lista)
    j=lista
    lista2=[]
    lista3=[]
    archivo.close()
    for posicion in range(0,len(lista)-1):       
        lista2.append(lista[posicion].strip("\n"))
    lista2.append(j[-1])
    for estrín in lista2:
        sublista=estrín.split(" ")
        lista3.append(sublista)
    return lista3
def transponer(matriz):    
    lista2=[]
    for a in range(0,len(matriz[0])):
        lista1=[]
        for b in range(0,len(matriz)):            
            lista1.append(matriz[b][a])
        lista2.append(lista1)
    return(lista2)
diagonal=[["A"],["SH"],["AGM"],["CRA"],["EO"],["I"]]
        

def sopaletras(nombre_archivo,palabras):
    p=(palabras[0]).upper()
    tabla=archivo_matriz(nombre_archivo)
    for a in range(0,len(tabla)):        
            if(p in "".join(tabla[a])):
                r="derecha"
                coord=[a,len(tabla[a])-len(p)]
                
    tabla=transponer(tabla)
    for a in range(0,len(tabla)):        
            if(p in "".join(tabla[a])):
                r="abajo"
                coord=[len(tabla[a])-len(p),a]
    for a in range(0,len(diagonal)):
     if(p in diagonal[a]):
        r="diagonal"        
        coord=[0,0]
                
    return [(p.lower(),coord,r)]


if __name__=="__main__":
    
   
    print(sopaletras("sopa.txt", ["casa"]))
    

           