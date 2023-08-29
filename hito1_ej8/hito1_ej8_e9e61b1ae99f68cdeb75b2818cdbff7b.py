n = int(input("Ingrese numero: "))
Unidades = n % 10
Decenas = n // 10 % 10
Centenas = n // 100 % 10
Miles = n // 1000 % 10
print(str(Miles) + 'M+' + str(Centenas) + 'C+' + str(Decenas) + 'D+' + str(Unidades) + 'U')
