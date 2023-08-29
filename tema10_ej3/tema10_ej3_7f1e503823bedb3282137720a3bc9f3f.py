def sopaletras(nombre_archivo, palabras):
  with open(nombre_archivo) as f:
    text = f.read()
    text = text.split('\n')
    dim = [int(text[0]), int(text[1])]
    text = text[2:]
  tablero = []
  for i in text:
    if len(i) != dim[1]:
      tablero.append([i[:dim[1]]])
      tablero.append([i[dim[1]:]])
    else:
      tablero.append(i)
  solucion = []
  for palabra in palabras:
    for i in range(len(tablero)):
      for j in range(len(tablero[i])):
        if palabra[0] == tablero[i][j]:
          if palabra in tablero[i]:
            solucion.append((palabra, [i, j], 'derecha
