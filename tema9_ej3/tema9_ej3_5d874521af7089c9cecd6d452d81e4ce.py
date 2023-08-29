def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje_codificado = "01101000,01101111,01101100,01100001"
    mensaje_decodificado = decodificar(mensaje_codificado)
    print("Mensaje decodificado:", mensaje_decodificado)