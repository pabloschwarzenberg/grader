def decodificar(mensaje):
    
    def binario_a_decimal(binario):
        posicion = 0
        decimal = 0
        binario = binario[::-1] 
        for digito in binario:
            multiplicador = 2**posicion
            decimal += int(digito) * multiplicador
            posicion += 1
        return decimal

    binarios = mensaje.split(",")
    decodificado = ""
    for i in binarios:
        caracter = chr(binario_a_decimal(i))
        decodificado += caracter
    return decodificado