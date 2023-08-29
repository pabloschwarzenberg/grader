def decodificar(mensaje):
    m=mensaje.split(",")
    lg=len(m)
    i=0
    m2=[]
    while i<lg:
        m1=int(m[i],2)
        m1=chr(m1)
        m2.append(m1)
        i=i+1
    mensaje="".join(m2)
    return mensaje


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         