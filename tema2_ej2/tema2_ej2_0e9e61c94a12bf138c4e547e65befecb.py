# completa el código de la función
def amigos(a,b):

  lista_a= []
  for i in range(1, a):
    if a % i==0:
      lista_a.append(i)
      

  suma_a = sum(lista_a)


  lista_b = []
  for i in range(1, b):
    if b % i==0:
      lista_b.append(i)
      


  suma_b = sum(lista_b)
  if suma_b == a and suma_a == b:
    return True
  else:
    return False 
           