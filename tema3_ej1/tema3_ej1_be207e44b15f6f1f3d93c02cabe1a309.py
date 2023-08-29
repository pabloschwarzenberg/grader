# Definir la función que recibe un número
def suma_divisores(numero):
  # Inicializar la suma en 0
  suma = 0
  # Recorrer los posibles divisores desde 1 hasta la mitad del número
  for divisor in range(1, numero // 2 + 1):
    # Si el número es divisible por el divisor
    if numero % divisor == 0:
      # Sumar el divisor a la suma
      suma += divisor
  # Si la suma es 1, el número es primo
  if suma == 1:
    primo = True
  else:
    primo = False
  # Retornar la suma y el valor de primo
  return suma, primo

# Si el programa se ejecuta como principal
if __name__ == "__main__":
  # Pedir al usuario que ingrese un número
  numero = int(input("Ingresa un número: "))
  # Llamar a la función con el número ingresado y guardar los resultados
  suma, primo = suma_divisores(numero)
  # Imprimir la suma y si el número es primo o no
  print("La suma de los divisores de", numero, "es", suma)
  if primo:
    print(numero, "es primo")
  else:
    print(numero, "no es primo")
