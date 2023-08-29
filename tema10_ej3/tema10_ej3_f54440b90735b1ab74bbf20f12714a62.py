def invertir_lista(lista):
  lista_invertida = []
  for a in range(-1, -len(lista) - 1, -1):
    lista_invertida.append(lista[a])
  inv = ""
  for a in lista_invertida:
    inv += a
  return inv



def sopaletras(nombre_archivo, palabras):
  archivo = open(nombre_archivo, "r")
  matriz = []
  for a in archivo:
    lista = []
    for n in a:
      n = n.lower()
      if n == " " or n == "\n":
        pass
      else:
        lista.append(n)

    matriz.append(lista)
  
  archivo.close()
  
  #HORIZONTAL
  for a in palabras:
    for n in range(len(matriz)):
      horizontal = ""

      for j in range(len(matriz[n])):
        horizontal += matriz[n][j]

      horizontal_inv = invertir_lista(matriz[n])
      indice = horizontal.find(a)
      indice_inv = horizontal_inv.find(a)

      if a in horizontal:
        return a, [n, indice], 'derecha'
      elif a in horizontal_inv:
        return (a, [n, indice_inv], "derecha")

  #VERTICAL
  
    for n in range(len(matriz[0])):
      lista_vertical = []
      vertical = ""

      for j in range(len(matriz)):
        lista_vertical.append(matriz[j][n])
        vertical += matriz[j][n]

      vertical_inv = invertir_lista(lista_vertical)
      indice = vertical.find(a)
      indice_inv = vertical_inv.find(a)
      
      if a in vertical:
        return a, [indice, n], "abajo"
      elif a in vertical_inv:
        return [(a, [indice_inv ,n], "abajo")]


  #DIAGONAL ABAJO

    columna = len(matriz) - 2
    contador = 1
    for n in range(columna, -1, -1):
      diagonal_abajo = []
      dia_abajo = ""
      dia_abajo += matriz[n][0]
      diagonal_abajo.append(matriz[n][0])
      aux = 0
      f = 1
      while contador != aux:
        dia_abajo += matriz[n + f][f]
        diagonal_abajo.append(matriz[n + f][f])
        aux += 1
        f += 1
      
      diagonal_abajo = invertir_lista(diagonal_abajo)
      col = (len(matriz) - 1) - contador
      indice = dia_abajo.find(a)

      

      if a in dia_abajo:
        return a, [col, indice], "diagonal"
      elif a in diagonal_abajo:
        return [(a, [0, 0], "diagonal")]
      
      contador += 1


    contador = 1
    fila = len(matriz[0]) - 2
    for n in range(fila, 0, -1):
      dia_arriba = ""
      diagonal_arriba = []

      diagonal_arriba.append(matriz[0][n])
      dia_arriba += matriz[0][n]
      aux = 0
      f = 1
      while contador != aux:
        dia_arriba += matriz[f][n + f]
        diagonal_arriba.append(matriz[f][n + f])
        aux += 1
        f += 1
      
      diagonal_arriba = invertir_lista(diagonal_arriba)
      fil = (len(matriz[0]) - 1) - contador
      colum = 0
      posicion = dia_arriba.find(a)

      if a in dia_arriba:
        return a, [colum + posicion, fil + posicion], "diagonal"
      elif a in diagonal_arriba:
        return [(a, [0, 0], "diagonal")]
      
      contador += 1


  #DIAGONAL ARRIBA

    contador = 1
    for n in range(1, len(matriz)):
      dia_arriba = ""
      diagonal_arriba = []
      
      dia_arriba += matriz[n][0]
      diagonal_arriba.append(matriz[n][0])
      aux = 0
      f = 1
      while aux != contador:
        dia_arriba += matriz[n - f][f]
        diagonal_arriba.append(matriz[n - f][f])

        aux += 1
        f += 1
      contador += 1
      diagonal_arriba = invertir_lista(diagonal_arriba)


      if a in dia_arriba:
        return [(a, [0, 0], "diagonal arriba")]
      elif a in diagonal_arriba:
        return [(a, [0, 0], "diagonal arriba")]
  

    contador = 1
    fila = len(matriz[0]) - 2
    columna = len(matriz) - 1
    for n in range(fila, 0, -1):
      dia_arriba = ""
      diagonal_arriba = []
      
      dia_arriba += matriz[columna][n]
      diagonal_arriba.append(matriz[columna][n])
      aux = 0
      f = 1
      while aux != contador:
        dia_arriba += matriz[columna - f][n + f]
        diagonal_arriba.append(matriz[columna - f][n + f])

        aux += 1
        f += 1
      contador += 1
      diagonal_arriba = invertir_lista(diagonal_arriba)

      if a in dia_arriba:
        return [(a, [0, 0], "diagonal arriba")]
      elif a in diagonal_arriba:
        return [(a, [0, 0], "diagonal arriba")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
  
    

           