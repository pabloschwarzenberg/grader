# completa el código de la función
def amigos(a,b):
  divisor = 1
  cont_a = 0
  cont_b = 0
  while divisor < a:
    resto = a%divisor
    if resto == 0:
      cont_a += divisor
    divisor += 1
  while divisor < b:
    resto = a%divisor
    if resto == 0:
      cont_b += divisor
    divisor += 1
  if cont_a == b and cont_b == a:
    return(True)
  else: 
    return(False)