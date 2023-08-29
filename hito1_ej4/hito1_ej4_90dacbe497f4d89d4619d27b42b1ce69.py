#decimal
decimal = int(input("Ingrese numero: "))
binario = 0
multiplicador = 1
while decimal != 0: # paso 3
    # pasos 1, 4 y 5 se multiplica el módulo por su multiplicador
    binario = binario + decimal % 2 * multiplicador
    decimal //= 2 
    multiplicador *= 10
print("resultado=",binario)