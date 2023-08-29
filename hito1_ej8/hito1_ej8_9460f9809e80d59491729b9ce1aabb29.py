#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")
numero = int(numero)
if (numero < 10 and numero > 0):
  unidades = int(numero % 10)
  print(unidades,"U")
if (numero < 100 and numero > 9):
  decenas = int(numero // 10)
  unidades = int(numero % 10)
  print(decenas,"D +", unidades,"U")
if (numero < 1000 and numero > 99):
  unidades = int(numero % 10)
  decenas = int((numero // 10) % 10)
  centenas = int(numero // 100)
  print(centenas,"C +", decenas,"D +", unidades,"U")
if (numero < 10000 and numero > 999):    
    unidades = int(numero % 10)
    decenas = int((numero // 10) % 10)
    centenas = int((numero // 100) % 10)
    miles = int(numero // 1000)
    print(miles,"M +", centenas,"C +", decenas,"D +", unidades,"U")