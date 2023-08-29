#Suma de los N primeros números
N = 0
while N<1:
  print("Porfavor ingrese un numero natural para N")
  N = int(input("N:"))
suma = N * (N+1)/2
print("la suma de los primeros",N,"números es",suma)