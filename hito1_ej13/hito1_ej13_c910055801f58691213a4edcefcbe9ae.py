#Factores Primos
a = int(input(">>> "))

factores = []
factoresprimos = []
is_prime = False

for num in range(1, int(a / 2)+1):
    if a % num == 0:
        factores.append(num)

factores.append(a)

for value in factores:
    if value > 1:
        is_prime = True
        for num in range(2,value):
          if value % num == 0:
              is_prime = False
    if is_prime:
        factoresprimos.append(value)


for item in factoresprimos:
    print(item)