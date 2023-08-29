#decodificadores

def decodificador(codigo):
    letras_cod = codigo.split(",")
    msj = ""
    for i in range(len(letras_cod)):
        msj = msj + chr(binario_decimal(letras_cod[i]))
    return msj

def binario_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

if __name__ == "__main__":
    print("Mensaje: " + decodificador("01101000,01101111,01101100,01100001"))