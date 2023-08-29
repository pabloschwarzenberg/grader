#Ordenar tres números
numbers = [int(input(" ingrese un numero entero ")), int(input(" ingrese un segundo numero entero ")), int(input(" ingrese un tercer numero entero "))]
counter = 0

while (counter < len(numbers)):
  innerCounter = 0
  while (innerCounter < len(numbers)):
    if (numbers[counter] < numbers[innerCounter]):
      numbers[innerCounter], numbers[counter] = numbers[counter], numbers[innerCounter]
    innerCounter += 1
  counter += 1

print(numbers)