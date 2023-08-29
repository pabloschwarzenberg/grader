def sopaletras(nombre_archivo,palabras):
  archivo=open("sopa.txt","r")
  archivo.close()
  return [(palabras[0],[0,0],"diagonal")]
def buscar_palabra_vertical(palabra, ):
  largo = len(palabra)
  fila = 0
  columna = 0
  for i in range(len(matriz[0])):
    for j in range(len(matriz) - largo + 1):
      palabra_prueba = ""
      for k in range(largo):
        palabra_prueba = palabra_prueba + matriz[j+k][i]
      if palabra_prueba.lower() == palabra:
        columna = i
        fila = j
  return (fila,columna)

def buscar_palabra_diagonal(palabra, matriz):
  largo = len(palabra)
  fila = 0
  columna = 0
  for i in range(len(matriz[0]) - largo + 1):
    for j in range(len(matriz) - largo + 1):
      palabra_prueba = ""
      for k in range(largo):
        palabra_prueba = palabra_prueba + matriz[i+k][j+k]
      if palabra_prueba.lower() == palabra:
        columna = j
        fila = i
  return (fila,columna)
def buscar_palabra_horizontal(palabra, matriz):
  largo = len(palabra)
  contador_linea = 0
  fila = 0
  columna = 0
  for linea in matriz:
    contador_columna = 0
    while contador_columna < len(linea) - (largo) + 1:
      subpalabra = linea[contador_columna : contador_columna + largo]
      palabra_prueba = ""
      for letra in subpalabra:
        palabra_prueba = palabra_prueba + letra
        if palabra_prueba.lower() == palabra:
          columna = contador_columna
          fila = contador_linea
      contador_columna += 1
    contador_linea += 1
  return (fila,columna)

matriz = sopaletras("sopa.txt","casa")
x, y = buscar_palabra_horizontal(palabra, matriz)
print("Palabra:", palabra ,"Línea:", x+1, "; Columna:",y+1)
palabra = "palindromo"
x, y = buscar_palabra_vertical(palabra, matriz)
print("Palabra:", palabra ,"Línea:", x+1, "; Columna:",y+1)
palabra = "grafo"
x, y = buscar_palabra_diagonal(palabra, matriz)
print("Palabra:", palabra ,"Línea:", x+1, "; Columna:",y+1)