def decodificar(mensaje):
    mensaje=mensaje.split(",")
    for i in range(len(mensaje)):
        binario=int(mensaje[i],2)
        letra=chr(binario)
        mensaje.pop(i)
        mensaje.insert(i,letra)
    mensaje="".join(mensaje)
        
        
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
