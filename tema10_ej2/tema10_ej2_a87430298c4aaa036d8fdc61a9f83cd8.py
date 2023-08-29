# Definir la función levenshtein que recibe dos palabras
def levenshtein(palabra1, palabra2):
  # Obtener la longitud de cada palabra
  n = len(palabra1)
  m = len(palabra2)

  # Crear una matriz de (n+1) x (m+1) con ceros
  matriz = [[0 for j in range(m+1)] for i in range(n+1)]

  # Llenar la primera fila y la primera columna con los valores de i y j
  for i in range(n+1):
    matriz[i][0] = i
  for j in range(m+1):
    matriz[0][j] = j

  # Recorrer el resto de la matriz, calculando la distancia según la fórmula
  for i in range(1, n+1):
    for j in range(1, m+1):
      # Verificar si los caracteres son iguales o no
      if palabra1[i-1] == palabra2[j-1]:
        costo = 0
      else:
        costo = 1
      
      # Elegir el mínimo entre las tres opciones posibles
      matriz[i][j] = min(matriz[i-1][j] + 1, matriz[i][j-1] + 1, matriz[i-1][j-1] + costo)
  
  # Obtener la distancia final que está en la última celda de la matriz
  distancia = matriz[n][m]

  # Verificar el valor de la distancia y retornar el string correspondiente
  if distancia > 1:
    return "+1"
  elif distancia == 0:
    return "0D"
  else:
    # Verificar si la operación fue una inserción, una eliminación o una sustitución
    if n == m:
      return "1S"
    else:
      return "IB"