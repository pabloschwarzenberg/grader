def sopaletras(nombre_archivo,palabras):
    
    #file=open("c:/tmp/sopa.txt","r")
    file=open(nombre_archivo,"r")
    lineas=[]
    for i in file:
        lineas.append(i.lower())
        
    
    for x in range(len(lineas)):
        h=lineas[x]
        lineas[x]=h.replace(" ","")
     
    
    file.close() 


    resultado=""
    resultado_f=[]
    
    for i in palabras:
        
        resultado=""
        frase=[i]
        
        ##########################
        # BUSCA HORINZONTALMENTE #
        ##########################
        i=0
        _found=False
        while(i<len(lineas)):
            if(lineas[i].find(frase[0])>=0):
                #print( "('" + frase[0] + "'" + ", ["+str(i)+", "+str(lineas[i].find(frase[0]))+"], 'derecha')")
                resultado=(frase[0],[i,lineas[i].find(frase[0])],'derecha')
                _found=True
                break
            i=i+1
        
        ##########################
        # BUSCA VERTICALMENTE    #
        ##########################
        
        if(_found==False):
            
            filas= len(lineas)
            columnas = len(lineas[0]) - 1
            _newPal=""
            linea_col=[]
            for i in range(columnas):
                for j in range(filas):
                    _newPal=_newPal + lineas[j][i]
                linea_col.append(_newPal)
                _newPal=""
        
            i=0
            _found=False
            while(i<len(linea_col)):
                if(linea_col[i].find(frase[0])>=0):
                    #print( "('" + frase[0] + "'" + ", ["+ str(linea_col[i].find(frase[0])) + ", "+str(i)+"], 'abajo')")
                    resultado=(frase[0],[linea_col[i].find(frase[0]),i],'abajo')
                    _found=True
                    break
                i=i+1
        
        ##########################
        # BUSCA DIAGONALMENTE    #
        ##########################
           
        if(_found==False): 
            diagonal=[]
            diagonal_pos=[]
            for j in range(4):
                d=""
                for i in range(len(lineas)):
                    p=lineas[i]
                    if( (i+j) < len(p)):
                        if(d==""):
                            diagonal_pos.append("["+str(i)+","+str(j)+"]")
                        d=d+p[i+j]
            
                diagonal.append(d.split())
            
            i=0
            _found=False
            while(i<len(diagonal)):
                if(diagonal[i][0].find(frase[0])>=0):
                    #print( "('" + frase[0] + "'" + ", " + diagonal_pos[i] +", 'diagonal')")
                    a=int(diagonal_pos[i][1])
                    b=int(diagonal_pos[i][3])
                    resultado=(frase[0],[a,b],'diagonal')
                    _found=True
                    break
                i=i+1
    
        resultado_f.append(resultado)
    return resultado_f   