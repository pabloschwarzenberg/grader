def distancia(palabra1, palabra2):
  e=dict()
  for i in range(len(palabra1)+1):
     e[i]=dict()
     e[i][0]=i
  for i in range(len(palabra2)+1):
     e[0][i] = i
  for i in range(1, len(palabra1)+1):
     for j in range(1, len(palabra2)+1):
        e[i][j] = min(e[i][j-1]+1, e[i-1][j]+1, e[i-1][j-1]+(not palabra1[i-1] == palabra2[j-1]))
  return e[len(palabra1)][len(palabra2)]
if __name__ == "__main__": 
  h = input('ingrese palabra1:  ')
  b = input('ingrese palabra2:  ')
  d = distancia(palabra1=h,palabra2=b)
  if d > 1:
      print('+',d)
  if d == 1:
      print('IB')
  if h == b:
      print('0D')
