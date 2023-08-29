#Conversión de Decimal a Binario
numero = float(input("ingrese un numero: "))
reciduo = " "

while(numero > 0):
    if(numero % 2 == 0):
        reciduo = "0" + reciduo
    else:
        reciduo = "1" + reciduo
    numero = numero // 2 #parte entera

print("resultado=", reciduo)