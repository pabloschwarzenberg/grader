#Conversión de Decimal a Binario
dec = int(input("N_dec: "))
binario = 0 
i = 0 
while(dec>0):
    cifra = dec % 2
    dec = int(dec//2)
    binario = binario + cifra*(10**i)
    i = i+1
print("resultado= ",binario)