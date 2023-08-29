#Conversión de Decimal a Binario
d = int(input("Porfavor inserte un numero decimal: "))
b = 0
i = 0
while (d>0):
    dig  = d%2
    d = int(d//2)
    b = b+dig*(10**i)
    i = i+1
print("resultado= ",b)
      