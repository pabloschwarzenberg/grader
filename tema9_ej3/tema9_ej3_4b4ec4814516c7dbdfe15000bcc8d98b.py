def decodificar(mensaje):
    mensaje=mensaje.replace(","," ")
    mensaje=mensaje.split()

    listafinal=[]
    
    for i in range(len(mensaje)):
        r=mensaje[i]    
        decimal=int(r,2)
        representacion=chr(decimal)
        listafinal.append(representacion)

    
    return ("".join(listafinal))
    
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
         