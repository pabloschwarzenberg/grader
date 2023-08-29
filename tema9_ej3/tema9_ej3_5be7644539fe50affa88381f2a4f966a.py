def decodificar(mensaje):
    bin1 = str(mensaje[0:8])
    numero1 = int(bin1, 2)
    letra1 = chr(numero1)

    bin2 = str(mensaje[9:17])
    numero2 = int(bin2, 2)
    letra2 = chr(numero2)

    bin3 = str(mensaje[18:26])
    numero3 = int(bin3, 2)
    letra3 = chr(numero3)

    bin4 = str(mensaje[27:35])
    numero4 = int(bin4, 2)
    letra4 = chr(numero4)
    mensaje = letra1+ letra2 + letra3 + letra4
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         