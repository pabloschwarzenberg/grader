#Suma de los N primeros números
suma=0
n=int(input("ingrese un numero: "))
for i in range(0,n+1):
  suma+=i
print(int(suma))