# completa el código de la función
def amigos(a,b):
  def divisores(numero):
    suma = 0
    for i in range(1,numero):
      if numero%i==0:
        suma += i
        return suma
  if divisores(a)==divisores(b) and a!=b:
    return True
  else:
    return False
           