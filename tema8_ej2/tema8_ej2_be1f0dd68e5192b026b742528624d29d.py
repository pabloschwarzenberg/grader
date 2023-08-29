def buscarTodas(a,b):
  l = []
  lf = []
  texto = ''

  for i in a:
    l.append(i)

  a = 0

  for i in l:
    if i==b:
      lf.append(l.index(i, a))
      a = l.index(i, a)+1

  for i in lf:
    texto = texto+str(i)+' '

  texto = texto[:-1]

  return texto