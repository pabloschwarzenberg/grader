def decimal_a_binario(numero_decimal):
numero_binario=0
multiplicador=1
while numero decimal !=0:
#se almacena el modulo en el orden correcto
numero_binario= numero_binario+ numero_decimal%2*multiplicador
numero_decimal//2=2
multiplicador*=10
return numero_binario
print(decimal_a_binario(5))