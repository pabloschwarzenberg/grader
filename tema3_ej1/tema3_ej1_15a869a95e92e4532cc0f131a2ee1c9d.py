# completa el código de la función
def suma_divisores(a):
  return
def suma_divisores(x):
    Suma = 0
    for i in range(1, x - 1):
        Resta = x % i
        if Resta != 0:
            continue
        Suma += i
    if Suma == 1:
        Primo = True
    else:
        Primo = False
    return Suma, Primo           