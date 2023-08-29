suma = 0
num = int(input("Ingrese un numero natural: "))

while (num <= 0):
	print("Error")
	num = int(input("Ingrese un numero natural: "))

for i in range (1, num+1):
	print(i)
	suma = suma + i
print("La suma de los primeros", num, "numeros es", suma)
      