#Conversión de Decimal a Binario
dc = int(input("Ingrese numero decimal: "))
bn = 0
i = 0
while (dc>0):
    dig  = dc%2
    dc = int(dc//2)
    bn = bn+dig*(10**i)
    i = i+1
print("resultado=",bn)