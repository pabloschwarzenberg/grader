def decodificar(mensaje):
    bloques = mensaje.split(",")
    mensaje = ""
    for letra in bloques:
      suma = 0
      for idx,digito in enumerate(letra[::-1]):
        suma += int(digito)*2**idx
      mensaje += chr(suma)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)