# completa el código de la función
def suma_divisores_propios(n):
   suma = 1
   divisor = 2;
   limite = n//2
   while divisor<=limite:
      if n%divisor == 0:
         suma += divisor
      divisor += 1;
   return suma
   
def amigos(n, m):
   suman = suma_divisores_propios(n)
   sumam = suma_divisores_propios(m)
   if suman == m and sumam == n:
      return True
   return False
           