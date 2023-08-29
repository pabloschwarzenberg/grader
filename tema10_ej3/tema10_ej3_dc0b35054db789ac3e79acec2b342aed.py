def sopaletras(nombre_archivo,palabras):
  # Leer el archivo y almacenar el tablero en una matriz
  archivo = open(nombre_archivo,"r")
  lineas = archivo.readlines()
  archivo.close()
  tablero = []
  for linea in lineas:
    fila = []
    for letra in linea.strip():
      fila.append(letra)
    tablero.append(fila)

  # Definir una función que busque una palabra en una dirección desde una posición
  def buscar_palabra(palabra,fila,columna,direccion):
    # Definir los incrementos de fila y columna según la dirección
    if direccion == "derecha":
      df = 0
      dc = 1
    elif direccion == "abajo":
      df = 1
      dc = 0
    elif direccion == "diagonal":
      df = 1
      dc = 1
    else:
      return False # Dirección inválida

    # Verificar si la palabra cabe en el tablero desde la posición inicial
    if fila + df * (len(palabra) - 1) >= len(tablero) or columna + dc * (len(palabra) - 1) >= len(tablero[0]):
      return False # La palabra se sale del tablero

    # Comparar cada letra de la palabra con el elemento correspondiente del tablero
    for i in range(len(palabra)):
      if palabra[i] != tablero[fila + df * i][columna + dc * i]:
        return False # La letra no coincide

    # Si todas las letras coinciden, retornar verdadero
    return True

  # Definir una lista vacía para almacenar los resultados
  resultados = []

  # Recorrer todas las posiciones del tablero
  for i in range(len(tablero)):
    for j in range(len(tablero[0])):
      # Recorrer todas las palabras a buscar
      for palabra in palabras:
        # Recorrer todas las direcciones posibles
        for direccion in ["derecha","abajo","diagonal"]:
          # Llamar a la función de búsqueda con los parámetros correspondientes
          if buscar_palabra(palabra,i,j,direccion):
            # Agregar el resultado a la lista con el formato solicitado
            resultados.append((palabra,[i,j],direccion))

  # Retornar la lista de resultados
  return resultados

           