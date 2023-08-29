# completa el código de la función
def suma_divisores(a):
     i = 1
     suma1 = 1
     while a > i :
         if a % i == 0 :
             suma1 = suma1 + a/i
             i = i + 1
         else :
             i = i + 1
     suma1 = suma1 - a
     if suma1 == 1:
         primo = True
     else :
         primo = False
     return suma1, primo

print(suma_divisores(73))
