# completa el código de la función
def suma_divisores(a):
  return
     # completa el código de la función
def suma_divisores(num):
    c = 0
    if num == 1:
        return (c,False)
    else:
        for i in range(1, num):
            if num%i == 0:
                c+=i
            else:
                continue
        for n in range(2, num):
            if num % n == 0:
                print("No es primo")
                return (c,False)
            else:
                print("Es primo")
                return (c,True)      