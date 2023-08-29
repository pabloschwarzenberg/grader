#Conversión de Decimal a Binario
def binary(ndec):
    nbin=''
    while ndec//2!=0:
        nbin=str(ndec%2)+nbin
        ndec=ndec//2
    return str(ndec)+nbin

num1=int(input("Introduce el número a convertir a binario: "))
print("Resultado=",(binary(num1)))