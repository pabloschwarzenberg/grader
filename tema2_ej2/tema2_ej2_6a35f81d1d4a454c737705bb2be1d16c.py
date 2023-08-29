#Numeros amigos
def raiz_cuadrada(n, error):
  # Esta función retorna la raíz cuadrada de n usando el método de Newton con un error máximo dado
  x = 1 # Valor inicial arbitrario
  while True: # Bucle infinito
    x1 = x - (x**2 - n) / (2 * x) # Aplicamos la fórmula de Newton
    if abs(x1 - x) < error: # Si la diferencia es menor que el error, paramos el bucle
      break
    x = x1 # Actualizamos el valor de x
  return x # Retornamos el valor aproximado de la raíz

def suma_divisores(n):
  # Esta función retorna la suma de los divisores propios de n usando una lista por comprensión y la función sum()
  divisores = [i for i in range(1, int(raiz_cuadrada(n, 0.0001)) + 1) if n % i == 0] # Obtenemos los divisores hasta la raíz cuadrada de n
  divisores.extend([n // i for i in divisores if i != 1 and i != n // i]) # Añadimos los divisores complementarios
  return sum(divisores) # Retornamos la suma de los elementos de la lista

def son_amigos(a, b):
  # Esta función retorna True si a y b son amigos, y False si no lo son
  return suma_divisores(a) == b and suma_divisores(b) == a


    print("Los números son amigos")

else:

    print("Los números no son amigos")
