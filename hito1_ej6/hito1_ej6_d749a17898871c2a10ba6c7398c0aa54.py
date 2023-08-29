# Entrada de los Numeros

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
c = int(input("Ingrese tercer Numero: "))

# Calculo de numeros de menor a mayor
if a > b and a > c:
  N_mayor = a
  if b > c:
    N_medio, N_menor = b, c
  else:
    N_medio, N_menor = c, b
if b > a and b > c:
  N_mayor = b
  if a > c:
    N_medio, N_menor = a, c
  else:
    N_medio, N_menor = c, a
elif c > b and b > c:
  N_mayor = c
  if a < b:
    N_medio, N_menor = a, b
  else:
    N_medio, N_menor = b, a
    
#salida

print(N_menor,",", N_medio,",", N_mayor)