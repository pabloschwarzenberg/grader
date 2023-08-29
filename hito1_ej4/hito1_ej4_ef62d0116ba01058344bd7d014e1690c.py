#Decimal a binario
def binario(decimal):
    binario1 = ''
    while decimal//2 != 0:
        binario1=str(decimal % 2)+binario1
        decimal=decimal//2
    return str(decimal)+binario1
numero_binario = int(input("Ingrese un decimal:  "))
print("resultado = ", binario(numero_binario))
      