# completa el código de la función
def suma_divisores(a):
  l = []
  largo = a
  for i in range(1,largo):
      if a%i == 0:
          l.append(i)        
  suma = sum(l)
  if suma == 1:
      return suma , True
  return suma , False