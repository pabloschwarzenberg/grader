#Conversión de Decimal a Binario
decimal = int(input("Introduce el número: "))

pri = bin(decimal)
strPri = str(pri)
strFin = strPri[2]+strPri[3]+strPri[4]+strPri[5]+strPri[6]+strPri[7]

print('resultado='+ strFin)