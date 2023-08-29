# completa el código de la función
def suma_divisores(a):
  # Esta función calcula la suma de los divisores de n sin incluir a n, y retorna esa suma y si n es primo o no
  suma = 0 # Inicializamos una variable para la suma
  for i in range(1, a): # Recorremos los posibles divisores desde 1 hasta n-1
    if a % i == 0: # Si i es divisor de n
      suma += i # Lo sumamos a la variable suma
  if suma == 1: # Si la suma es igual a 1
    primo = True # El número es primo
  else: # Si no
    primo = False # El número no es primo
  return suma, primo # Retornamos la suma y el valor booleano de primo

# Probamos la función con algunos ejemplos
if __name__ == "__main__":
  print(suma_divisores(6)) # Debe retornar (6, False)
  print(suma_divisores(7)) # Debe retornar (1, True)
  print(suma_divisores(12)) # Debe retornar (16, False)