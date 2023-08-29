def buscarTodas(a,b):
    respuesta= ''
    a=list(a)
    for i in range(0,len(a)):
        t=0    
        while t<len(a):
            if a[i]==b:
                respuesta=respuesta + str(i)+' '
                
                break
            else:
                t=t+1
    respuesta=list(respuesta)
    respuesta=respuesta[0:len(respuesta)-1]
    respuesta=''.join(respuesta)
    
    return respuesta 
           