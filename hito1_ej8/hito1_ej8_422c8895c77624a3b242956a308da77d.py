#Descomponer un número
numero = input("Ingrese un número (debe ser de 4 dígitos): ")
while len(numero) > 4:
  numero = input("El número debe tener 4 dígitos. Por favor, ingrese otro número: ")
if len(numero) == 4:
  print(str(int(numero[0])) + "M+" + str(int(numero[1])) + "C+" + str(int(numero[2])) + "D+" + str(int(numero[3])) + "U")
elif len(numero) == 3:
  print(str(int(numero[0])) + "C+" + str(int(numero[1])) + "D+" + str(int(numero[2])) + "U")
elif len(numero) == 2:
  print(str(int(numero[0])) + "D+" + str(int(numero[1])) + "U")
elif len(numero) == 1:
  print(str(int(numero[0])) + "U")
else:
  print("El número ingresado no tiene una longitud válida.")


      