# Función que calcula el costo de alinear dos caracteres
def costo(c1, c2):
  if c1 == c2:
    return 0 # No hay costo si son iguales
  elif c1 == "_" or c2 == "_":
    return 1 # Hay un costo de 1 si hay un espacio
  else:
    return 2 # Hay un costo de 2 si son diferentes

# Función que alinea dos secuencias de ADN usando programación dinámica
def alinear(adn1, adn2):
  # Crear una matriz de (len(adn1) + 1) x (len(adn2) + 1) con ceros
  m = [[0 for j in range(len(adn2) + 1)] for i in range(len(adn1) + 1)]
  
  # Llenar la primera fila y la primera columna con el costo acumulado de insertar espacios
  for i in range(1, len(adn1) + 1):
    m[i][0] = m[i-1][0] + costo(adn1[i-1], "_")
  for j in range(1, len(adn2) + 1):
    m[0][j] = m[0][j-1] + costo("_", adn2[j-1])
  
  # Llenar el resto de la matriz con el mínimo costo de alinear cada subsecuencia
  for i in range(1, len(adn1) + 1):
    for j in range(1, len(adn2) + 1):
      m[i][j] = min(m[i-1][j] + costo(adn1[i-1], "_"), # Insertar un espacio en adn2
                    m[i][j-1] + costo("_", adn2[j-1]), # Insertar un espacio en adn1
                    m[i-1][j-1] + costo(adn1[i-1], adn2[j-1])) # No insertar espacios
  
  # Reconstruir el alineamiento óptimo desde la esquina inferior derecha de la matriz
  i = len(adn1)
  j = len(adn2)
  alineado = "" # El segundo string alineado con el primero
  while i > 0 or j > 0:
    if i > 0 and j > 0 and m[i][j] == m[i-1][j-1] + costo(adn1[i-1], adn2[j-1]):
      # Caso en que no se insertan espacios
      alineado = adn2[j-1] + alineado
      i -= 1
      j -= 1
    elif i > 0 and m[i][j] == m[i-1][j] + costo(adn1[i-1], "_"):
      # Caso en que se inserta un espacio en adn2
      alineado = "_" + alineado
      i -= 1
    else:
      # Caso en que se inserta un espacio en adn1
      alineado = adn2[j-1] + alineado
      j -= 1
  
  return alineado

# Programa principal que recibe las entradas y llama a la función alinear
adn1 = input("Ingrese el primer string: ")
adn2 = input("Ingrese el segundo string: ")
alineado = alinear(adn1, adn2)
print("El segundo string alineado con el primero es:")
print(alineado)
  