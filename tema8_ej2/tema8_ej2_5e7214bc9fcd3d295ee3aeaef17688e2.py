def  buscarTodas(mensaje,busqueda ):

    codigo=[]

    for i  in range(len(mensaje)):
    
        letra = mensaje[i]
    
        if letra == busqueda :
            codigo.append(str(i)) 
    
    codigo_2= " ".join(codigo) 
    
    
    return codigo_2