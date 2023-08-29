#Suma de los N primeros números
N = int(input("Ingrese cuantos numeros desea sumar: "))
suma = 0
total = 0
while suma < N:
  suma = suma + 1
  total = suma + total
n = str(N)
t = str(total)
print ("los primeros " + (n) +" números suman "+ (t))