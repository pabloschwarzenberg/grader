# completa el código de la función
def suma_divisores(a):
    divisor = 1
    losdivisores = -a
    while divisor <= a:
        if 0 == a%divisor:
          losdivisores += divisor 
          divisor += 1
        else:
          divisor += 1
    if losdivisores == 1:
      return losdivisores, True
    else:
      return losdivisores, False