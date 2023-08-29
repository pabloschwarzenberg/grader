num = int(input("Número: "))

factores = []
div = 2

while div <= num:
    if num % div == 0:
        factores.append(div)
        num /= div
    else:
        div += 1

for i in factores:
    print(i)

