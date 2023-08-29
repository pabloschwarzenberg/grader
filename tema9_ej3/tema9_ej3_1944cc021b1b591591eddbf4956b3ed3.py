def decodificar(mensaje):
    # Convertir la cadena de entrada en una lista de números binarios
    numeros_binarios = mensaje.split(',')
    
    # Convertir cada número binario a su equivalente decimal y luego a su letra correspondiente
    letras = [chr(int(num_binario, 2)) for num_binario in numeros_binarios]
    
    # Unir todas las letras para formar el mensaje descifrado
    mensaje_descifrado = ''.join(letras)
    
    return mensaje_descifrado

if __name__ == "__main__":
    mensaje = "01101000,01101111,01101100,01100001"
    
    print(decodificar(mensaje))         