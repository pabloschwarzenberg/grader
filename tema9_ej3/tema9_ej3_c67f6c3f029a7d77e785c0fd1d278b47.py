def decodificar(mensaje):
    a=mensaje.split(",")
    palabra=[]
    for i in a:
        b=int(i,2)
        c=chr(b)
        palabra.append(c)
    p=str(palabra).replace("['","").replace("', '","").replace("']","")
    return p

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         