def levenshtein(palabra1, palabra2):
  d=dict()
  for i in range(len(palabra1)+1):
     d[i]=dict()
     d[i][0]=i
  for i in range(len(palabra2)+1):
     d[0][i] = i
  for i in range(1, len(palabra1)+1):
     for j in range(1, len(palabra2)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not palabra1[i-1] == palabra2[j-1]))
  resultado= d[len(palabra1)][len(palabra2)]

  re=''
  if resultado>1:
      re='+1'
  if resultado == 0:
      re = '0D'
  if resultado==1 and len(palabra1)==len(palabra2):
      re='1S'
  if resultado==1 and len(palabra1)!=len(palabra2):
      re='IB'
  return re

print(levenshtein('gallina','gallo'))

if __name__=="__main__":
    pass
