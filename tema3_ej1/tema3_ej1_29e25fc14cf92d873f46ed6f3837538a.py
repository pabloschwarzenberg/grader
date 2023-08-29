# completa el código de la función
def suma_divisores(a):
  division = [i for i in range(1,a) if a%i == 0]
  suma = sum(division)
  if suma == 1:
    return suma,True
  return suma,False