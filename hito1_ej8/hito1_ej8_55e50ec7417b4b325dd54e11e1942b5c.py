#Descomponer un número
n = int(input("Ingrese numero: "))
unidad = n % 10
decena = n // 10 % 10
centena = n // 100 % 10
mil = n // 1000 % 10
print(str(mil) + 'M+' + str(centena) + 'C+' + str(decena) + 'D+' + str(unidad) + 'U')