def trans_bin(cod):
    lista=list(cod)
    lista.reverse()
    suma=0
    i=0
    for x in lista:
        x=int(x)
        suma=suma+(2**i)*x
        i+=1
    return chr(suma)
def decodificar(mensaje):
    mensaje=mensaje.split(",")
    palabra=[]
    for u in mensaje:
        r=trans_bin(u)
        palabra.append(r)
    return "".join(palabra)
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         