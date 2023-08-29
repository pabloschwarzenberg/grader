def decodificar(mensaje):
  # Dividir el mensaje por comas
  lista_binaria = mensaje.split(",")
  # Crear una lista vacía para guardar las letras
  lista_letras = []
  # Recorrer cada número binario de la lista
  for binario in lista_binaria:
    # Convertir el número binario a decimal usando la función int
    decimal = int(binario, 2)
    # Convertir el número decimal a letra usando la función chr
    letra = chr(decimal)
    # Agregar la letra a la lista de letras
    lista_letras.append(letra)
  # Unir las letras de la lista para formar el mensaje descifrado
  mensaje_descifrado = "".join(lista_letras)
  # Retornar el mensaje descifrado
  return mensaje_descifrado

# Ejemplo de uso de la función
print(decodificar("01101000,01101111,01101100,01100001"))
