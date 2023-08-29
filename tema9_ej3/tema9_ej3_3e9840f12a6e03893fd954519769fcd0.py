def decodificar(mensaje):
    for caracter in mensaje:
        mensaje=mensaje.replace(",","")
    return ''.join(chr(int(mensaje[i*8:i*8+8],2)) for i in range(len(mensaje)//8))

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         