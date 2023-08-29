#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
  d=dict()
  for indice in range(len(palabra1)+1):
     d[indice]=dict()
     d[indice][0]=indice
  for indice in range(len(palabra2)+1):
     d[0][indice] = indice
  for indice in range(1, len(palabra1)+1):
     for j in range(1, len(palabra2)+1):
        d[indice][j] = min(d[indice][j-1]+1, d[indice-1][j]+1, d[indice-1][j-1]+(not palabra1[indice-1] == palabra2[j-1]))

  if d[len(palabra1)][len(palabra2)]>1:
      resultado="+1"
  if d[len(palabra1)][len(palabra2)]==1 :
      resultado="IB"
  if d[len(palabra1)][len(palabra2)]==1 and len(palabra1)==len(palabra2) :
      resultado="1S"
  if d[len(palabra1)][len(palabra2)]==0:
      resultado="0D"
  return resultado



if __name__=="__main__":
     palabra1=input("")
     palabra2=input("")
     dist=levenshtein(palabra1,palabra2)
     print(dist)

     pass
           