#Conversión de Decimal a Binario
decimal = 33

# PROCEDIMIENTO
binario = 0
i = 0
while (decimal>0):
    digito  = decimal%2
    decimal = int(decimal//2)
    binario = binario+digito*(10**i)
    i = i+1
# SALIDA
print("en binario: ",binario)