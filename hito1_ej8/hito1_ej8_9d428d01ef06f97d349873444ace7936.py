#Descomponer un número
numero = int(input("Ingrese numero: "))
unidad = numero % 10
decena = ((numero % 100) - unidad)//10
centena = ((numero % 1000) - unidad - decena)//100
mil = ((numero % 10000) - unidad - decena - centena)//1000
print(unidad)
print(decena)
print(centena)
print(mil)
if mil == 0:
    print(str(centena)+"C", "+", str(decena)+"D", "+", str(unidad)+"U")
if mil == 0 and centena == 0:
    print(str(decena)+"D", "+", str(unidad)+"U")
if mil == 0 and centena == 0 and decena == 0:
    print(str(unidad)+"U")
else:
    print(str(mil)+"M", "+", str(centena)+"C", "+", str(decena)+"D", "+", str(unidad)+"U")