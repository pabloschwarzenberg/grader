def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
mensaje_codificado = "01101000,01101111,01101100,01100001"
mensaje_descifrado = decodificar(mensaje_codificado)
print(mensaje_descifrado)  # Resultado: "hola"
        