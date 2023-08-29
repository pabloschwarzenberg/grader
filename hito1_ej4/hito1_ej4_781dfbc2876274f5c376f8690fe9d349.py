#Conversión de Decimal a Binario
def hac_bin(num):
    bina=""
    if num<=0:
        return "0"
    while num>0:
        resid=(int(num%2))
        num=(int(num/2))
        bina=str(resid) + bina
    return bina


num=int(input("Ingrese Numero: "))
binanum = hac_bin(num)
print("resultado=", binanum)