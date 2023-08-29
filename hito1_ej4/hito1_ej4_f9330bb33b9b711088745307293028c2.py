#Conversión de Decimal a Binario
dec = int(input("Ingrese número decimal: "))
#valores
bina = 0

i = 0


while (dec>0):
    dig  = dec%2
    dec = int(dec//2)
    bina = bina+dig*(10**i)
    i = i+1
print("resultado=",bina)

    