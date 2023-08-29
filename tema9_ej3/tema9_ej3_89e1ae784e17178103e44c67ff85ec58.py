def decodificar(mensaje):
    a=mensaje.split(",")
    acumulacion=""
    for i in a:  #a es una lista de strings va a recorrer cada elemento de la lista
        exponente=0
        sum=0
        for j in range(len(i)-1,-1,-1): #recorre cada elemento de la i
            sum=sum+ (2**exponente)*int(i[j])
            exponente+=1
        acumulacion+=chr(sum)
    return acumulacion

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)