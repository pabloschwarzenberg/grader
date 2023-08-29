def decodificar(mensaje):
  palabra = ""
  # Se convierte el número binario a decimal / ascii
  ascii_caracter = list()
  codigos = mensaje.split(",")
  for codigo in codigos:
    multiplo = 7
    suma = 0
    for numero in codigo:
      suma += int(numero) * (pow(2,multiplo))
      multiplo -= 1
    ascii_caracter.append(suma)
  #Se convierte de ascii a alfabetico y se genera la palabra.
  for valor in ascii_caracter:
    palabra += chr(valor)
  return palabra
         
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         