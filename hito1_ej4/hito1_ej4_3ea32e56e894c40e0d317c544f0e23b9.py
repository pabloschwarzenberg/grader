#Conversión de Decimal a Binario
numero=int(input("ingrese el numero que decea transformar a binario: "))

def binarios(decimal):
    binario=''
    while decimal//2!=0:
        binario=str(decimal%2)+binario
        decimal=decimal//2
    return str(decimal)+binario
print("resultado=",end="")
print(binarios(numero))