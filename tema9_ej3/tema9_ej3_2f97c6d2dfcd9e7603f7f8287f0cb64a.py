def decodificar(mensaje):
  caracter = input("ingrese caracter: ")
  codigo = ord(caracter)
  print(codigo)
  return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         