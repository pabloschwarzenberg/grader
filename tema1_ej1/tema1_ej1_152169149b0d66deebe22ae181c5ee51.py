#Suma de los N primeros números
      #La suma de los primeros n numeros naturales está dada por (n*(n + 1))/2. Crea un programa que reciba como parámetro un número N y luego imprima la suma de los N primeros números naturales.

#ingreso de valor.
numero = input("ingresa un numero: ")

#verificacion de valor.
try:
    numero = int(numero)
except ValueError:
    print("ERROR: no ingresaste un numero")
    exit()

suma_naturales = (numero * (numero + 1)) / 2
print(suma_naturales)