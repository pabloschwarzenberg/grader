# Definir la función que recibe un número
def numero_perfecto(numero):
  # Inicializar la suma de los divisores en 0
  suma = 0
  # Recorrer los posibles divisores desde 1 hasta la mitad del número
  for divisor in range(1, numero // 2 + 1):
    # Si el número es divisible por el divisor
    if numero % divisor == 0:
      # Sumar el divisor a la suma
      suma += divisor
  # Si la suma es igual al número
  if suma == numero:
    # El número es perfecto
    return True
  else:
    # El número no es perfecto
    return False

# Si el programa se ejecuta como principal
if __name__ == "__main__":
  # Pedir al usuario que ingrese un número
  numero = int(input("Ingresa un número: "))
  # Llamar a la función con el número ingresado y guardar el resultado
  resultado = numero_perfecto(numero)
  # Imprimir el resultado
  if resultado:
    print(numero, "es un número perfecto")
  else:
    print(numero, "no es un número perfecto")
