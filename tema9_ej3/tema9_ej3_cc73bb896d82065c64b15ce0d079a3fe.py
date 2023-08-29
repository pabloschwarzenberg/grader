def decodificar(mensaje):
    mensaje1=mensaje[0:8]
    mensaje2=mensaje[9:17]
    mensaje3=mensaje[18:26]
    mensaje4=mensaje[27:35]
    bina1 = int(mensaje1,2)
    bina2 = int(mensaje2,2)
    bina3 = int(mensaje3,2)
    bina4 = int(mensaje4,2)
    letra1 = chr(bina1)
    letra2 = chr(bina2)
    letra3 = chr(bina3)
    letra4 = chr(bina4)
    mensaje = letra1+letra2+letra3+letra4
    
    
    
    return mensaje


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         