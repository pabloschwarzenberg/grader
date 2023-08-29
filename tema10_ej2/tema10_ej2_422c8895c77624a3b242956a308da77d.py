#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
  n = len(palabra1)
  m = len(palabra2)

  matriz = [[0 for j in range(m+1)] for i in range(n+1)]

  for i in range(n+1):
    matriz[i][0] = i
  for j in range(m+1):
    matriz[0][j] = j

  for i in range(1, n+1):
    for j in range(1, m+1):

      if palabra1[i-1] == palabra2[j-1]:
        costo = 0
      else:
        costo = 1
      
      matriz[i][j] = min(matriz[i-1][j] + 1, matriz[i][j-1] + 1, matriz[i-1][j-1] + costo)
  

  distancia = matriz[n][m]

  if distancia > 1:
    return "+1"
  elif distancia == 0:
    return "0D"
  else:
    if n == m:
      return "1S"
    else:
      return "IB"
           