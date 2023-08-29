#Ordenar tres números
numbers = []
for i in range(3):
    n = int(input("Ingrese un numero: "))
    numbers.append(n)
numbers.sort()
print(numbers)