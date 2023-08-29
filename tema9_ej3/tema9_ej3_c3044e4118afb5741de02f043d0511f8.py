def decodificar(mensaje):
    
    uno = str(mensaje[0:8])
    numeros1 = (int(str(uno), 2))
    w1 = chr(numeros1)
    
    
    
    dos = str(mensaje[10:17])
    numeros2 = (int(str(dos), 2))
    w2 = chr(numeros2)

    
    tres = str(mensaje[19:26])
    numeros3 = (int(str(tres), 2))
    w3 = chr(numeros3)

    
    cuatro = str(mensaje[28:35])
    numeros4 = (int(str(cuatro), 2))
    w4 = chr(numeros4)
    
    
    
    palabraCompleta = w1 + w2 + w3 + w4
     
    return palabraCompleta




if __name__ == "__main__":
    
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
    
    