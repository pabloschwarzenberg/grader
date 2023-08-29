def decodificar(mensaje):
  numeros_binarios = mensaje.split(',')
  texto_descifrado = ""
  
  for numero_binario in numeros_binarios:
    decimal = int(numero_binario, 2)
    letra = chr(decimal)
    texto_descifrado += letra
  return texto_descifrado
  

if __name__ == "__main__":
    mensaje_cifrado = "01101000,01101111,01101100,01100001"
    resultado = decodificar(mensaje_cifrado)
    print(resultado)
         