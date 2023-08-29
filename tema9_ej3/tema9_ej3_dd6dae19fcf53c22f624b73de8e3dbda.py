def decodificar(mensaje):

    lisMensaje=mensaje.split(",")
    lisLetras=[]
    for i in range (0,len(lisMensaje)):
        decimal=int(lisMensaje[i],2)
        caracter=chr(decimal)
        lisLetras.append(caracter)
        
    mensaje= "".join(lisLetras)
        
    
    return mensaje
    

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         