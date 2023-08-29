# completa el código de la función
def suma_divisores(a):
    if a==1:
      return 1
    for i in range(2,a+1):
      if a%i == 0: 
        return a + suma_divisores(a//i)