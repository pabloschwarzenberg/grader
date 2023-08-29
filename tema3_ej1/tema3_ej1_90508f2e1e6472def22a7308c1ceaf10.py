# completa el código de la función
def suma_divisores(a):
  divicion = [i for i in range(1,a) if a%i==0]
  R = sum(divicion)
  if R == 1:
      return R, True
  return R, False

           