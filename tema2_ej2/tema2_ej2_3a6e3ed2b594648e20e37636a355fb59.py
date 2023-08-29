# completa el código de la función
def amigos(a, b):
 perro = 0
 waton = 0
 for i in range(1, a):
   if a % i == 0:
     perro += i

 for x in range(1, b):
   if b % x == 0:
     waton += x

 return perro == b and waton == a