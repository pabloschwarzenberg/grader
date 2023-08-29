#Conversión de Decimal a Binario
def decimal_a_binario(no_dec):
    if no_dec<=0:
        return'0'
        bnr = ''
    while no_dec>0:
        re= int(no_dec%2)
        n = int(no_dec//2)
        b = str(re)+bnr
    return bnr
no_dec = float(input('Ingrese un decimal: '))
bnr=  decimal_a_binario(no_dec)
print('El número ',no_dec,'en binario es ',(decimal_a_binario(no_dec)),'')
























