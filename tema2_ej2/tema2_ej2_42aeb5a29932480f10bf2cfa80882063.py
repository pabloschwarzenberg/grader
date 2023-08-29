# completa el código de la función
def amigos(a,b):
   suma_divisores_a = sum([i for i in range(1, a) if a % i == 0])
   suma_divisores_b = sum([i for i in range(1, b) if b % i == 0])
    
   if suma_divisores_a == b and suma_divisores_b == a:
        return True
   else:
       return False
           