# completa el código de la función
def suma_divisores(a):
    m = 0
    divisor = 1
    while divisor < a :
        if a % divisor == 0 :
            m += divisor
        divisor = divisor + 1
    if m == 1 :
      return m, True
    else :
      return m, False
           