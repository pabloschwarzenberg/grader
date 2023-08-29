#Conversión de Decimal a Binario
n_dec=int(input('Ingrese numero decimal: '))

n_bin=""

while n_dec!=1:
    if n_dec%2==1:
        n_bin="1"+n_bin
        n_dec=n_dec//2
    elif n_dec%2==0:
        n_bin="0"+n_bin
        n_dec = n_dec // 2
n_bin=int("1"+n_bin)
print("resultado=",n_bin)
