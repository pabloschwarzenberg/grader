def levenshtein(a, b):
  d=dict()
  for i in range(len(a)+1):
     d[i]=dict()
     d[i][0]=i
  for i in range(len(b)+1):
     d[0][i] = i
  for i in range(1, len(a)+1):
     for j in range(1, len(b)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not a[i-1] == b[j-1]))

  if d[len(a)][len(b)] == 0:
      resultado = "0D"

  if d[len(a)][len(b)] > 1:
      resultado = "+1"

  if d[len(a)][len(b)] == 1:
      if len(a) == len(b):
          resultado = "1S"
      else:
          resultado = "IB"
  return resultado        