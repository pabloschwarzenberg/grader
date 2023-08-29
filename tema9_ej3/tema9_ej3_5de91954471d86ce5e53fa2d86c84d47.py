def decodificar(mensaje):
    lista=mensaje.split(',')
    mensaje=''
    for codigo in lista:
        mensaje+=chr(int(codigo,2))
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         