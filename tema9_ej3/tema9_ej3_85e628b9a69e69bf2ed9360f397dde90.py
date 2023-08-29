def decodificar(mensaje):
    codigos=mensaje.split(",")
    l=[]
    for i in codigos:
        c=7
        suma=0
        for j in range(8):
            suma+=int(i[j])*2**c
            c=c-1
        l.append(suma)
    palabra=""
    for i in l:
        letra=chr(i)
        palabra=palabra+letra
    mensaje=palabra            
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         