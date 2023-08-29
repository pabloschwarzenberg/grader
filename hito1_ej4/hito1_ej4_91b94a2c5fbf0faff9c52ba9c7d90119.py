#Conversion decimal a binario
numero_decimal = float(input("Ingrese un número decimal: "))

numero_binario = 0
multiplicador = 1

while numero_decimal != 0: 
    numero_binario = numero_binario + numero_decimal % 2 * multiplicador
    numero_decimal //= 2 
    multiplicador *= 10 

print("Resultado=", numero_binario)