#Conversión de Decimal a Binario
def nino(decimal):
    binario=""
    while decimal//2!=0:
          binario=str(decimal%2)+binario
          decimal=decimal//2
    return str(decimal)+binario
a=int(input())
print("resultado=",nino(a))
 