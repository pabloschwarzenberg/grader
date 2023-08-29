def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = []
    
    for binario in numeros_binarios:
        decimal = int(binario, 2)
        letra = chr(decimal)
        letras.append(letra)
    
    mensaje_decodificado = ''.join(letras)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje_codificado = "01101000,01101111,01101100,01100001"
    resultado = decodificar(mensaje_codificado)
    print(resultado)
