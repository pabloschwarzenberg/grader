#Factores Primos
num = int(input('Ingresa un número entero: '))
primo = 2
while num > 1:
    if num%primo == 0:
        print(primo)
        num = num/primo
        primo = 2
    else:
        primo += 1