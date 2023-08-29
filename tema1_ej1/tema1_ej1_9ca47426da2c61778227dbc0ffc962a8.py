#Suma de los N primeros números
n=int(input("Ingrese un numero: "))
if n<0:
   print("El numero ingresado no es natural")
else:
   o= n*(n+1)/2
   print("La suma de los numeros naturales son: ",o)