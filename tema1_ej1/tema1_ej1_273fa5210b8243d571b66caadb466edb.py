#Suma de los N primeros números
N=int(input("Inserte un número natural: "))
if(N<=0):
  print("El número elegido no es un número natural.")
else:
  R=N*(N+1)/2
  print("La suma de todos los números naturales hasta ",N,"es ",R,".")