def decodificar(mensaje):
    cadena=""
    valores=mensaje.split(",")
    decimales=[]
    d=1
    
    for x in valores:
        x=list(x)
        x.reverse()
        t=0
        for tt in x:
            if (tt == "1"):
                t=t+d
            d=d*2
        d=1
        decimales.append(t)
    for carry in decimales:
        cadena=cadena+str(chr(carry))
    return cadena
    
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         