#Factores Primos
num = int(input('Ingresa un numero: '))


primos = []
for i in range(2,num+1):
    while num % i == 0:
        primos.append(i)
        num = num / i

for primo in primos:
    print(primo)     