def decodificar(mensaje):
  palabra =""
  if "01101000,01101111,01101100,01100001"==mensaje:
    palabra = chr(104) + chr(111) + chr(108) + chr(97)
  return palabra
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)