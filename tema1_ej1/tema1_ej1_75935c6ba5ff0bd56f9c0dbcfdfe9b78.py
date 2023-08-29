#Suma de los N primeros números
N=int(input("ingrese un numero natural "))
while (N<0):
  print("porfavor, ingrese un numero natural positivo para así iniciar el calculo")
suma= (N*(N+1)/2)
print("la suma de los " ,N, "numeros naturales equivale a ",suma)      