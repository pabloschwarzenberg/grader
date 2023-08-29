def decodificar(mensaje):
    result = ""
    for caracter in mensaje.split(","):
      caracter = int(caracter, 2)
      result += chr(caracter)
    return result

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         