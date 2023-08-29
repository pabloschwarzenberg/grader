def decodificar(mensaje):
    resultado = ""
    secuencia = ""
    caracter = 0
    for c in mensaje:
      if c == ",":
        caracter = int(secuencia, 2)
        resultado += chr(caracter)
        secuencia = ""
      else:
        secuencia += c
    caracter = int(secuencia, 2)
    resultado += chr(caracter)
    return resultado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)