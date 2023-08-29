# completa el código de la función
def suma_divisores(a):
  divisores_a = []
  for valor in range(1,a):
    if a%valor == 0:
      divisores_a.append(valor)
  suma =  0
  for i in divisores_a:
    suma += i
  if suma == 1:
    return suma,True
  if suma != 1:
    return suma,False
           