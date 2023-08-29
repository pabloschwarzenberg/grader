#Conversión de Decimal a Binario
NumeroDecimal=int(input("Ingrese Numero decimal: "))
Incremento = 0
Binario = 0
while True:
    Resto = NumeroDecimal%2
    Binario = Binario + (int(Resto)*(10**Incremento))
    Incremento = Incremento+1
    NumeroDecimal = NumeroDecimal/2
    if NumeroDecimal == 0:
        break

print("resultado="+str(Binario))