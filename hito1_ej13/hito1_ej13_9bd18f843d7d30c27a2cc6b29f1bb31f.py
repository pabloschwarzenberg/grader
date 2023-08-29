#Factores Primos
n = int(input('ingresa un numero para descomponer en sus factores primos: '))
if  n == 2:
    print(2)
for i in range(2,n):
    while n % i == 0:
        n = n/i
        print(i)