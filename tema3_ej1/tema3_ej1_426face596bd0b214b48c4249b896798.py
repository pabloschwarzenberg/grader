# completa el código de la función
def suma_divisores(a):
 suma = 0
 esPrimo = False
 for divisor in range(1,a):
   if (a % divisor) == 0 :
     suma += divisor
 if suma == 1:
   esPrimo = True
 return suma, esPrimo