#Conversión de Decimal a Binario
def dec2bin(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]
    
num=int(input('numero'))

x= dec2bin(num)

print('resultado=' , x)

