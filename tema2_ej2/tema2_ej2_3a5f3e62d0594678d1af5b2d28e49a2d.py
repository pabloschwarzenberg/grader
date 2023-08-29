# completa el código de la función
def amigos(a,b):
  lista = []
  lista_b =[]
  for i in range(1,a-1):
    if a%i==0:
      lista.append(i)
  for i in range(1,b-1):
    if b%i==0:
      lista_b.append(i)
  s1=0
  for i in lista:
    s1+=i
  s2=0
  for i in lista_b:  
    s2+=i
  if s1==b or s2==a:
    return True
  else:
    return False
           