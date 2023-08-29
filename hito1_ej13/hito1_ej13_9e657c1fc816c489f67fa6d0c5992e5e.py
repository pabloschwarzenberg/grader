#Factores Primos
num = int(input())

primos = []
for i in range(2, num+1):
    while num % i == 0:
        primos.append(i)
        num = num / i

for n in primos:
    print(n)
    