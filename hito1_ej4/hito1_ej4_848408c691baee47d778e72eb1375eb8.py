#Conversión de Decimal a Binario me costo encontrar una manera rapida sin usar un while normal ni """"
NumeroDecimalEntero = int(input("Ingresa un número decimal: "))
ResultadoBlanco = ""

while NumeroDecimalEntero > 0:
    DivisonRestoExacto = int(NumeroDecimalEntero % 2)
    NumeroDecimalEntero = int(NumeroDecimalEntero / 2)
    ResultadoBlanco = str(DivisonRestoExacto) + ResultadoBlanco
print("resultado=", ResultadoBlanco)