#Conversión de Decimal a Binario
def binario(decimal):
     binario = ''
     while decimal//2!=0:
        binario=str(decimal%2)+binario
        decimal=decimal//2
     return str(decimal)+binario

numero = int(input())

print("resultado="+binario(numero))