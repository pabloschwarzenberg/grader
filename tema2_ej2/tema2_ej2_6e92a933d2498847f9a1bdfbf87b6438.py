# completa el código de la función
def suma(nro):
  lista=[]
  if nro==2:
    return 3
  if nro==1:
    return 1
  for i in range(2,nro):
    if nro%i==0:
      lista.append(i)
    return sum(lista)
def amigos(a,b):
  if a!=b and suma(a)==suma(b):
    return True
  else:
    return False
           