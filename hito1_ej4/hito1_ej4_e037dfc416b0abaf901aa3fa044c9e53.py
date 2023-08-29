number = int(input('Ingresa un entero: '))
collection = []
while number > 0:
    divide = int(float(number % 2))
    collection.append(divide)
    number = (number - divide)/2
print("resultado="+''.join(str(char) for char in collection[::-1]))
