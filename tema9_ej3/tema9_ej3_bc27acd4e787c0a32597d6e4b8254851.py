def decodificar(mensaje):
    mensaje=mensaje.split(",")
    mensaje1=[]
    for numero in mensaje:
        mensaje1.append(int(numero,2))
    a=""
    for numero in mensaje1:
        a=a+a.join(chr(numero))
    return a

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
        