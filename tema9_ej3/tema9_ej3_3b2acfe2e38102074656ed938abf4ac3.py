def decodificar(mensaje):
    mensaje=mensaje.split(",")
    m=0
    k=len(mensaje)-1
    cadena=[]
    while k>=m:
       n=(int(mensaje[m],2))
       pegar=chr(n)
       cadena.append(pegar)
       m=m+1
    cadena="".join(cadena)
    return cadena

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
