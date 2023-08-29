# completa el código de la función
def amigos(a,b):
  if a == b:
    return False
    
  suma_de_divisores_a = sum(divisores(a))
  suma_de_divisores_b = sum(divisores(b))
  return suma_de_divisores_a == b and suma_de_divisores_b == a
    
def divisores(numero):
  divisores = []
  for i in range(1, numero):
    if numero % i ==0:
      divisores.append(i)
  return divisores
          
print(amigos(220, 264))
print(amigos(1000, 1200))
print(amigos(220, 221))