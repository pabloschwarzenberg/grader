#Suma de los N primeros números
def sumar(N):
  return (N * (N+1))/2
  
N = int(input("Hola, ingresa el número que se utilizará como parámetro: "))

suma = sumar(N)

print("La suma de los N números naturales es: ", suma)
print("el programa a finalizado, adiós")