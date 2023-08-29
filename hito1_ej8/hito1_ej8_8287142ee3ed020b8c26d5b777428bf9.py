#Descomponer un número

digito = input("Ingresa el digito de hasta 4 numeros: ")

if len(digito) == 4:
  print("La descompocision de tu numero de 4 digitos es: \n", digito[0], "M +", digito[1], "C +", digito[2], "D +", digito[3], "U")

if len(digito) == 3:
  print("La descompocision de tu numero de 3 digitos es: \n", digito[0], "C +", digito[1], "D +", digito[2], "U")

if len(digito) == 2:
  print("La descompocision de tu numero de 2 digitos es: \n", digito[0], "D +", digito[1], "U")

if len(digito) == 1:
  print("Las unidades que tienes son: \n", digito[0], "U")

if len(digito) > 4:
  print("Cantidad de caracteres no permitido")