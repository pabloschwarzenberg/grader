# completa el código de la función
def suma_divisores(a):
   
    r = 0
    x = a
    while a > 1:
        if x % a == 0:
            n = x / a
            r = n + r
            a = a - 1
        else:
            a = a - 1
    if r != 1:
      return r, False
    else:
      return r, True

           

