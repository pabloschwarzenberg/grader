# completa el código de la función
def suma_divisores(a):
  resultado = [ i for i in range(1, a + 1) if a % i == 0]
  resultado.remove(a)
  suma = 0
  for elemento in resultado:
   suma += elemento
 
  if suma == 1:
      primo = True
  else:
      primo = False

  return suma , primo

print(suma_divisores(14))
