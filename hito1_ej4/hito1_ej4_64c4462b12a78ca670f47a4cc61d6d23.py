#Conversión de Decimal a Binario

dec = int(input('N: '))
a = 0
n = 0

while dec != 0:
    if dec == 1:
        a = a + (dec % 2) * (10 ** n)
        break
    a = a + (dec % 2) * (10 ** n)
    dec = dec // 2
    n += 1
    
print ('resultado=', a)