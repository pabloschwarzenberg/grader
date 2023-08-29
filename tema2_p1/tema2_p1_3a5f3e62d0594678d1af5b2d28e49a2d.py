# completa el código de la función
def es_primo(a):
  lista = []
  for i in range(1,a+1):
    if a%i==0:
      lista.append(i)
  s1=0
  for i in lista:
    s1+=i
  if s1==a+1:
    return True
  else:
    return False