def decodificar(mensaje):
    mensaje=mensaje.split(",")

    cero=int(mensaje[0])
    binario1=(int(str(cero),2))
    one=chr(binario1)
    uno=int(mensaje[1])
    binario2=(int(str(uno),2))
    two=chr(binario2)
    dos=int(mensaje[2])
    binario3=(int(str(dos),2))
    three=chr(binario3)
    tres=int(mensaje[3])
    binario4=(int(str(tres),2))
    four=chr(binario4)

    mensaje=one+two+three+four
    
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         