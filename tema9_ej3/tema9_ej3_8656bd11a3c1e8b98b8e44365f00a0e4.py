def decodificar(mensaje):
    texto_plano = ""
    for binario in mensaje.split(","):
        valor = int(binario, 2)
        texto_plano += chr(valor)
    return texto_plano

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         