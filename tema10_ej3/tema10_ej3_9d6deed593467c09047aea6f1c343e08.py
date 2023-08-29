def buscar_palabra_en_fila(palabra, fila, tablero):
  for i in range(len(tablero[fila])):
    if tablero[fila][i:i+len(palabra)] == palabra:
      return (fila, i, "derecha")
    return None

def buscar_palabra_en_columna(palabra, columna, tablero):
  for i in range(len(tablero)):
    if "".join([tablero[j][columna] for j in range(i,i+len(palabra))]) == palabra:
      return (i, columna, "abajo")
    return None

def buscar_palabra_en_diagonal(palabra, fila, columna, tablero):
  diagonal = [tablero[fila+i][columna+i] for i in range(len(palabra))]
  if "".join(diagonal) == palabra:
    return (fila, columna, "diagonal")
  return None
  
def buscar_palabra(palabra, tablero):
  for i in range(len(tablero)):
    for j in range(len(tablero[i])):
      if palabra[0] == tablero[i][j]:
        posibles_resultados = [buscar_palabra_en_fila(palabra, i, tablero),buscar_palabra_en_columna(palabra, j, tablero),buscar_palabra_en_diagonal(palabra, i, j, tablero)]
        for resultado in posibles_resultados:
          if resultado is not None:
            return resultado
      return None  
      
  for palabra in palabras:
    resultado_palabra = buscar_palabra(palabra, tablero)
    if resultado_palabra is not None:
      resultado.append((palabra, resultado_palabra[:2], resultado_palabra[2]))
        
    return resultado
      
    