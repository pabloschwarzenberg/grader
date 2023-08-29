#Suma de los N primeros números
N = eval(input("Ingrese un número natural: "))
if (N > 0 and type(N) == int):
  formula = N * (N+1) / 2
  print("El total de la suma desde el 1 hasta el", N, "es",formula)
else:
  print("El número ingresado no es natural")