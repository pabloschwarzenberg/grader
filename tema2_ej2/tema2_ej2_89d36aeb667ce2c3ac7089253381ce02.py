# completa el código de la función
def amigos (a,b):
    if a!=b:
         suma = 0
         for i in(range(1, a +1)):
             if a % i == 0:
                 suma +=i

         suma2 = 0
         for i in range(1, b+1):
             if b % i == 0:
                 suma2 +=i

         if suma2-b == a and suma-a ==b:
             return True
    return False           