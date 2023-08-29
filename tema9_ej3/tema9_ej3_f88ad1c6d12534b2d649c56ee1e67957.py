## ENTRADA DE DATOS - PROCESO - SALIDA

## FUNCIÓN:

def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = []

    for binario in numeros_binarios:
        decimal = int(binario, 2)
        letra = chr(decimal)
        letras.append(letra)

    mensaje_descifrado = "".join(letras)
    return mensaje_descifrado

## LLAMADA FUNCIÓN E IMPRESIÓN EN PANTALLA

if __name__ == "__main__":
    mensaje_codificado = "01101000,01101111,01101100,01100001"
    mensaje_descifrado = decodificar(mensaje_codificado)
    print(mensaje_descifrado)