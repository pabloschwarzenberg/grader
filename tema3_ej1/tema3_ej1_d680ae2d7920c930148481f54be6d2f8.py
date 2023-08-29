#completa el codigo de la funcion
def suma_divisores(num):
   suma = 0
   for x in range(1, num):
       if num % x == 0:
          suma += x
   if suma == 1:
       return suma, True
   else:
       return suma, False      