#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Create a list with the user input numbers
lst = [num1, num2, num3]

# Sort the list in ascending order
lst.sort()

# Join the elements and print them separated by commas
result = ','.join(map(str, lst))
print(result)
