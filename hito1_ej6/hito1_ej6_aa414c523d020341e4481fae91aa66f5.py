#Ordenar tres números
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Ingrese el tercer numero: "))

if number1 < number2 and number2 < number3:
  print(str(number1) + "," + str(number2) + "," + str(number3))
elif number1 < number3 and number3 < number2:
  print(str(number1) + "," + str(number3) + "," + str(number2))
elif number2 < number1 and number1 < number3:
  print(str(number2) + "," + str(number1) + "," + str(number3))
elif number2 < number3 and number3 < number1:
  print(str(number2) + "," + str(number3) + "," + str(number1))
elif number3 < number2 and number2 < number1:
  print(str(number3) + "," + str(number2) + "," + str(number1))
else:
  print(str(number3) + "," + str(number1) + "," + str(number2))