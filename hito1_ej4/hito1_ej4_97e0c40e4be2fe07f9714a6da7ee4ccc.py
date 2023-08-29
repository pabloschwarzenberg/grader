decimal = int(input("N decimal: "))
bi = 0 
i = 0 
while(decimal>0):
    numero = decimal % 2
    decimal = int(decimal//2)
    bi = bi + numero*(10**i)
    i = i+1
print("resultado= ",bi)