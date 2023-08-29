def decodificar(mensaje):
    numbinarios = mensaje.split(',')
    letras = [chr(int(numbinario, 2)) for numbinario in numbinarios]
    msjdescifrado = ''.join(letras)
    return msjdescifrado


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         