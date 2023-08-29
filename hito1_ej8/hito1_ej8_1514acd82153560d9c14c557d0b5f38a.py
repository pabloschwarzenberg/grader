#Descomponer un número
import random as rnd
n = int(input("Ingresa un número de 4 cifras: "))

print(n)

u = n%10
n //= 10

d = n%10
n //= 10

c = n%10
n //= 10

print(str(n)+"M+" +str(c)+"C+" +str(d)+"D+" +str(u)+"U")