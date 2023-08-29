# por favor escribe aquí tu función
def es_primo(numero):
  print("El numero es", numero)
  
primo = input("inserte un numero")

for numero in str(primo):
  for divisor in range(2, primo):
    if int(numero) // int(divisor) != 0:
      print("El numero es primo", True)
    else:
      print("El numero no es primo", False)