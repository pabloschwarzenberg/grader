def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    l=[]
    lista=[]
    lista2=[]
    lista3=[]
    lista4=[]
    lista5=[]

    for linea in archivo:
        linea.strip()
        linea.split(" ")
        l.append(linea)
    for i in range(len(l)):
        a="".join(l[i])
        lista.append(a)
        for j in range(len(palabras)):
            if palabras[j] in lista[i]:
                b=lista[i].find(palabras[j])
                return [(palabras[j],[i,b],"derecha")]
                
    for j in range(len(l[0])):
        for i in range(len(l)):
            lista2.append(l[i][j])
            for k in range(len(lista2)):
                a="".join(lista2[k])
                lista3.append(a)
                for m in range(len(palabras)):
                    if palabras[m] in lista3[i]:
                        b=lista3[i].find(palabras[m])
                        return [(palabras[m],[i,b],"abajo")]
    
    
            
        
    
    
    
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    pass

           