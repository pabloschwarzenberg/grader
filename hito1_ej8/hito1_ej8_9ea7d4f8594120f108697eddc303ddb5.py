#Descomponer un número
num = input("Ingrese un número entero mayor o igual a cero y menor que 10000:")
digitos = list(num)
if len(digitos) == 4:
  print(digitos[0],"M+",digitos[1],"C+",digitos[2],"D+",digitos[3],"U")
if len(digitos) == 3:
  print(digitos[0],"C+",digitos[1],"D+",digitos[2],"U")
if len(digitos) == 2:
  print(digitos[0],"D+",digitos[1],"U")
if len(digitos) == 1:
  print(digitos[0],"U")      