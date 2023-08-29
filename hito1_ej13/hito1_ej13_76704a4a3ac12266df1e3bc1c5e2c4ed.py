#Factores Primos
n=int(input("Ingresa un numero: "))
for divisor in range(2,n):
    if n%divisor==0:
     print(divisor)