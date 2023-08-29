#Suma de los N primeros números
print("Ingrese un número")
n = int(input())
for i in range(1,n+1):
  suma = i*(i+1)//2
  print(suma)