#Descomponer un número

numero = int(input('Ingresa un número de hasta 4 digitos: '))

dU = numero%10
numero = numero//10

dD = numero%10
numero = numero//10

dC = numero%10
numero = numero//10

dM = numero%10
numero = numero//10

print(dM,'M', '+', dC,'C', '+', dD,'D', '+', dU,'U')