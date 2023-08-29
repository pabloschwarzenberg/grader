# Definir una función que alinee dos secuencias de ADN
def alinear_secuencias(adn1, adn2):
  # Crear una variable para almacenar el resultado
  resultado = ""
  # Crear dos índices para recorrer las secuencias
  i = 0 # Índice para el primer string
  j = 0 # Índice para el segundo string
  # Mientras no se haya llegado al final de ninguna de las secuencias
  while i < len(adn1) and j < len(adn2):
    # Si los caracteres en las posiciones i y j son iguales, agregar el caracter del segundo string al resultado y avanzar ambos índices
    if adn1[i] == adn2[j]:
      resultado += adn2[j]
      i += 1
      j += 1
    # Si no, agregar un guión bajo al resultado y avanzar solo el índice del primer string
    else:
      resultado += "_"
      i += 1
  # Si quedan caracteres en el segundo string, agregarlos al resultado
  if j < len(adn2):
    resultado += adn2[j:]
  # Retornar el resultado
  return resultado

# Pedir al usuario que ingrese las dos secuencias de ADN
adn1 = input("Ingrese la primera secuencia de ADN: ")
adn2 = input("Ingrese la segunda secuencia de ADN: ")

# Llamar a la función alinear_secuencias con las secuencias ingresadas
alineacion = alinear_secuencias(adn1, adn2)

# Imprimir el resultado
print(alineacion) 