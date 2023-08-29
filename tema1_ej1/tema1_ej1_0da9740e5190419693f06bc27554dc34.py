#Suma de los N primeros números
N = int(input("ingrese un numero natural: "))

if(N<1):
 print("numero ingresado no es natural")
else:
 print((N*(N+1))/2)      