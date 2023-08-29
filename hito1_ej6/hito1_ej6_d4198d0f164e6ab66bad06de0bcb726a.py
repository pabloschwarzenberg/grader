#Ordenar tres números
numbers = []
for i in range(3):
    numbers.append(int(input(str(i+1)+": Ingresa un Numero ")))
numbers.sort()
print(",".join(map(str,numbers)))