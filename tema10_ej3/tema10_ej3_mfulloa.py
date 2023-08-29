def sopaletras(nombre_archivo,palabras):
    palabras=palabras.append(palabras)
    letras=[]
    archivo=open(nombre_archivo,"r")
    for i in archivo:
        i=i.strip().split(" ")
        letras.append(i)
    archivo.close()
    l1=[]
    for j in range(len(letras)):
        for k in letras[j]:
            if palabras in l1:
                    return (l,"[0,",j,"]","derecha")
    l2=[]
    for j in range(len(letras)):
        l2.append(letras[j][0])
        if palabras in l2:
                return (l,"[0,0]","abajo")
    l3=[]
    for j in range(len(letras)):
        l3.append(letras[j][1])
        if palabras in l3:
                return (l,"[1,0]","abajo")
    l4=[]
    for j in range(len(letras)):
        l4.append(letras[j][2])
        if palabras in l4:
                return (l,"[2,0]","abajo")
    l5=[]
    for j in range(len(letras)):
        l5.append(letras[j][3])
        if palabras in l5:
                return (l,"[3,0]","abajo")
    l6=[]
    for j in range(len(letras)):
        l6.append(letras[j][j])
        if palabras in l6:
                return (l,"[0,0]","diagonal")                
        

if __name__=="__main__":
    palabras=list(input("Ingrese palabra: "))
    print(sopaletras("sopa.txt",palabras))