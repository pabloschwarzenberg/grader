def binario_a_decimal(binario):
        posicion = 0
        decimal = 0
        binario = binario[::-1] #invierte la cadena
        for digito in binario:
            multiplicador = 2**posicion
            decimal += int(digito) * multiplicador
            posicion += 1
        return decimal

def decodificar(mensaje):
    # Funcion para pasar un número binario a base decimal
    
    binarios = mensaje.split(",")
    decodificado = ""
    for i in binarios:
        caracter = chr(binario_a_decimal(i))
        decodificado += caracter
    return decodificado

if __name__ == "__main__":
    print(decodificar("01101000,01101111,01101100,01100001"))        