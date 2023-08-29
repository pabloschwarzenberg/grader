def sopaLetras(nombre_archivo,palabras):
    res=[]
    archivo=open(nombre_archivo,"r")
    archiList=archivo.readlines()
    sopa=[]
    for renglon in archiList:
        #En este paso genero una lista donde cada elemento es un string, cada string es una linea de la sopa de letras
        #Esto lo hago para trabajar con mayor comodidad
        renglon=renglon[:-1]
        renglon=renglon.split(" ")
        letras=""
        for letra in renglon:
            letras+=letra
        sopa.append(letras)

    for palabra in palabras:
        encontrado=False #Esta variable la defino para que cuando encuentre la palabra deje de trabajar el programa 
        iniX=False
        iniY=False
        orientacion=False
        #Estas 4 variables de arriba las defino en False para que no me tire error si la palabra no esta en la sopa
        if not(encontrado):
            #horizontal
            k=0
            while k<len(sopa) and not(encontrado): #con la variable K recorro las filas y con las i las columnas
                i=0
                while i<len(sopa[0]):
                    if palabra==sopa[k][i:len(palabra)] and not(encontrado):
                        encontrado=True
                        iniX=i
                        iniY=k
                        orientacion="horizontal"
                    i+=1
                k+=1
        
        if not(encontrado):
            #vertical
            k=0
            while k < len(sopa) and not(encontrado):
                i=0
                while i<len(sopa[0]) and not(encontrado):
                    if palabra[0]==sopa[k][i]:
                        reso=""
                        for aux in range(k,len(sopa)):
                            reso+=sopa[aux][i]
                            if reso==palabra:
                                encontrado=True
                                iniX=i
                                iniY=k
                                orientacion="vertical"
                    i+=1
                k+=1
        
        if not(encontrado):
            #Diagonal
            k=0
            while k<len(sopa)and not(encontrado):
                i=0
                while i < len(sopa[0]) and not(encontrado):
                    reso=""
                    aux1=i
                    if palabra[0]==sopa[k][i] and not(encontrado):
                        for aux in range(k,len(sopa)):
                            if aux1<len(sopa[0]):
                                reso+=sopa[aux][aux1]
                            aux1+=1
                            if reso==palabra:
                                encontrado=True
                                iniX=i
                                iniY=k
                                orientacion="diagonal"
                            
                    i+=1
                k+=1
        tupla=(palabra,[iniX,iniY],orientacion)
        res.append(tupla)
    
    archivo.close()

    return res