def decodificar(mensaje):
    a=mensaje.split(",")
    lista=[]
    for numero in a:
        suma=0
        for i in range(0, 8):
            suma=suma+int(numero[i])*2**(7-i)
        lista.append(suma)
    for i in range(0,len(a)):
        lista[i]=chr(lista[i])
    return "".join(lista)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         