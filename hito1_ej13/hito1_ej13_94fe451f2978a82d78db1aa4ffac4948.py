#Factores Primos
x = int(input('\nIngresa un número: '))

for i in range(1, x+1):
    if x%i==0:
        print(i)
        input()