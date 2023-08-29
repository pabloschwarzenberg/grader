r1 = son_amigos(1, 2) # Llamar a la función son_amigos

  # Función auxiliar que calcula la suma de los divisores de un número
  def suma_divisores(n):
    suma = 0
    for i in range(1, n): # Se excluye al mismo número
      if n % i == 0: # Si i es divisor de n
        suma += i # Se suma a la suma
    return suma
    
  # Se verifica si la suma de los divisores de a es igual a b y viceversa
  return suma_divisores(a) == b and suma_divisores(b) == a
