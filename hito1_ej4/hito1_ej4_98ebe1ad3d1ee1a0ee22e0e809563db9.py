#Conversión de Decimal a Binario
numero = input("ingrese Nº: ")
num = int(numero)
par = 2

NumDiv = 0
acumP = ''
acumIP = ''
acumX = ''
acumZ = ''
while num > 0:

    if num % 2 == 0 :
        NumDiv = num // par
        num = NumDiv
        acumP = str(acumP)+str("0")
        acumX = acumP[0:1]
        
    else:
        NumDiv = num // par
        acumIP = str(acumIP)+str("1")
        num = NumDiv
        acumX = acumIP[0:1]

    acumZ = acumX+acumZ
      
print("resultado = ",acumZ)     