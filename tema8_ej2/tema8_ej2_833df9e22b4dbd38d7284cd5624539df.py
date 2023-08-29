def buscarTodas(a,b):
    posicion=""
    c=0
    for i in a:
        if i==b:
            s=(a.index(b,c))
            posicion+=(" "+str(s))
            c=s+1
           
            
    return(posicion[1:])
            
    





            
    
            
            