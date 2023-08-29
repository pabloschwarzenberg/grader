def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
  def imprimir_numeros_ascii(s):
  for i in s:
    print(ord(i))

s = input("Ingrese string")
imprimir_numeros_ascii(s)       