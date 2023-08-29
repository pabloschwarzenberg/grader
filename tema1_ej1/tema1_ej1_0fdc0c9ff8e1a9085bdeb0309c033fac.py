#Suma de los N primeros números
 
N = int(input("Ingrese cantidad de numeros naturales a sumar:"))

for i in range(1,N+1):
  sum = (i*(i+1))/2
  
print(sum)
  