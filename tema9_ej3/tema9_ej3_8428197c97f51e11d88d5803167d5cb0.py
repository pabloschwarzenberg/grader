def decodificar(mensaje):
    # Separa cada número binario de 8 dígitos por comas
    numeros = mensaje.split(",")
    # Convierte cada número binario a su equivalente decimal y luego a su letra o símbolo correspondiente en ASCII
    letras = [chr(int(numero, 2)) for numero in numeros]
    # Une todas las letras y retorna el resultado
    return "".join(letras)
         