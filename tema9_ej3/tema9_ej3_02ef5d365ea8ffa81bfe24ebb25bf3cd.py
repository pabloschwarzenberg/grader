def decodificar(mensaje):
  binaries = mensaje.split(',')
  text = ''
  for binary in binaries:
    decimal = int(binary, 2)
    character = chr(decimal)
    text += character + ''
  return text

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         