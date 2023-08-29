def buscarTodas(frase,letra):
   
    largo=len(frase)
    i=0
    p="S"
    respuesta=str()
    print("largo:" , largo)
    posicion=str()
    while i<largo and i>=0 and posicion!="-1":
    
        posicion=str(frase.find(letra,i))

        print("Indice:" , i)
        print("posicion:", posicion)
        if posicion!="-1":
        
            if p=="S":
            
                p="N"
                respuesta=respuesta+posicion  
                print("primera resouesta:" ,respuesta)
            else:
                respuesta=respuesta+" "+posicion
                print("respuesta:" , respuesta)
        else:
            break
    
        i=int(posicion)+1
    return(respuesta)
    
            
           