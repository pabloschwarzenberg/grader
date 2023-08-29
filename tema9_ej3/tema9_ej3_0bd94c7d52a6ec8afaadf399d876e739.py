def decodificar(mensaje):

    def binario_a_ascii(mensaje):
        valor = int(mensaje,2)
        return chr(valor)

    def binario_a_texto(mensaje):
        texto_plano = ""
        for binario in mensaje.split(","):
            texto_plano += binario_a_ascii(binario)
        return texto_plano
    return binario_a_texto(mensaje)


if __name__ == "__main__":
    #mensaje= int(input("ingrese el código a decodificar: "))
    print(decodificar(mensaje))
    mensaje = "01101000,01101111,01101100,01100001"
         