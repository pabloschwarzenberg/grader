def decodificar(mensaje):
    lista=mensaje.split(',')
    palabra=''
    for i in lista:
        dec=int(str(i),2)
        letra=chr(dec)
        palabra+=letra
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

         