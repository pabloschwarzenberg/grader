#Factores Primos
numero = int(input('numero: '))
div = []
i = 2
while i<numero:
    if numero % i==0:
        div.append(i)
        i = i + 1
    else:
        i = i + 1
for primos in div:
    if numero % i==0:
        print(primos)