def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios
    numeros_binarios = mensaje.split(",")
    caracteres = []
    for numero_binario in numeros_binarios:
        caracter = chr(int(numero_binario, 2)) #Pasarlo de binario a letra
        print(caracter)
        caracteres.append(caracter)


    mensaje_descifrado = "".join(caracteres)

    return mensaje_descifrado

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

    