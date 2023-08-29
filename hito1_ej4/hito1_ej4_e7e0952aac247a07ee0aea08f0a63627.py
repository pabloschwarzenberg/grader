#Conversión de Decimal a Binario
n = eval(input("Ingrese un numero: "))
binario = ""
if (n > 0):
    while(n > 0):
        if (n%2 == 0):
            binario = "0" + binario
        else:
            binario = "1" + binario
        n = int(n/2)

print("resultado=",binario)

    