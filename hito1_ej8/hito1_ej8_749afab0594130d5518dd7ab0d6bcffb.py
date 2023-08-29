#Descomponer un número
def descomposicion_numeros():
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

  if numero < 0 or numero > 9999:
      print("Ingrese un numero válido")
      return

unidades = numero % 10
decenas = (numero // 10) % 10
centenas = (numero // 100) % 10
miles = (numero // 1000) % 10

print(miles, "M +", centenas, "C +", decenas, "D +", unidades, "U")


descomposicion_numeros()
