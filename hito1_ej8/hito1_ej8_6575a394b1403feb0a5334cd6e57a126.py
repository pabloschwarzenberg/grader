#Descomponer un numero digito por digito
n = int(input('Ingresa un numero entero de maximo 4 digitos:' ))
unidad = str(n % 10)
decena = str((n // 10) % 10)
centena = str((n // 100) % 10)
miles = str((n // 1000) % 10)
print(miles + 'M' + ' ' + '+' + ' ' + centena + 'C' + ' ' + '+' + ' ' + decena + 'D' + ' ' + '+' + ' ' + unidad + 'U')