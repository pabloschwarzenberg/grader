def decodificar(mensaje):
    numeros=mensaje.split(",")
    mensaje="hol"
    for numero_binario in numeros:
        numero_decimal=int(numero_binario,2)
    letra = chr (numero_decimal)
    mensaje += letra
    return mensaje
if __name__=="__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print("mensaje")