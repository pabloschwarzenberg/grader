g=(input('ingrese secuencia(solo letras)')).upper()
l=[]
i=0
while i<len(g):
  l.append(g[i])
  i+=1
i=0
while i<len(l):
  if l[i] in ['A','C','T','G']:
    secuencia=True
  else:
    secuencia=False
    break
  i+=1
if secuencia==True:
  print('secuencia correcta')
elif secuencia==False:
  print('secuencia incorrecta')