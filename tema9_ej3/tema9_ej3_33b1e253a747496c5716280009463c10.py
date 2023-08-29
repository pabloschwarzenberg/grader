def decodificar(cadena):
    resultado = ""
    numeros = cadena.strip().split(",")
    for numero in numeros:
        # Convertimos el número de binario a decimal usando 2 Bytes
        numero = int(numero, 2)
        # Convertimos el número de decimal a caracter usando la función chr()
        resultado += chr(numero)
    return resultado

if __name__ == "__main__":
    # Ejemplo de uso
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)