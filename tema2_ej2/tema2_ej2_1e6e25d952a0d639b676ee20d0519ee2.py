# completa el código de la función
def lista_divisores(c):
  divisores = []
  for i in range(1, c + 1):
      if c % i == 0:
          divisores.append(i)
  return divisores
  
def suma_divisores(divisores):
  suma = 0
  for i in range(1, len(divisores)):
    suma += divisores[i]
  return suma  

def amigos(a,b):
  x = lista_divisores(a)
  y = lista_divisores(b)
  s = suma_divisores(x)
  v = suma_divisores(y)
  if s == v and a != b:
    return True
  else:
    return False