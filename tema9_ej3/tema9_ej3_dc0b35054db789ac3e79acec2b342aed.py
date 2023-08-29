# Definir la función decodificar
def decodificar(mensaje):
  # Dividir el mensaje por las comas y guardar la lista resultante en una variable
  lista_binaria = mensaje.split(",")
  # Crear una lista vacía para guardar las letras
  lista_letras = []
  # Recorrer la lista binaria con un ciclo for
  for binario in lista_binaria:
    # Convertir el número binario a decimal usando la función int con base 2
    decimal = int(binario, 2)
    # Convertir el número decimal a la letra o símbolo que representa usando la función chr
    letra = chr(decimal)
    # Agregar la letra a la lista de letras
    lista_letras.append(letra)
  # Unir las letras de la lista con el método join y guardar el resultado en una variable
  mensaje_decodificado = "".join(lista_letras)
  # Retornar el mensaje decodificado como el resultado de la función
  return mensaje_decodificado
