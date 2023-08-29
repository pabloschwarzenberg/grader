#Descomponer un número
var_Numero = int(input("Ingresa un número: "))
while (len(str(var_Numero)) > 4):
    var_Numero = int(input("Ingresa un número: "))
var_Millares = (var_Numero - (var_Numero % 1000)) / 1000
var_ModMillares = var_Numero % 1000
var_Centenas = (var_ModMillares - (var_ModMillares % 100)) / 100
var_ModCentenas = var_ModMillares % 100
var_Decenas = (var_ModCentenas - (var_ModCentenas % 10)) / 10
var_ModDecenas = var_ModCentenas % 10
var_Unidades = var_ModDecenas
if (len(str(var_Numero)) == 4):
    print(str(int(var_Millares)) + "M + " + str(int(var_Centenas)) + "C + " + str(int(var_Decenas)) + "D + " + str(int(var_Unidades)) + "U")
elif (len(str(var_Numero)) == 3):
    print(str(int(var_Centenas)) + "C + " + str(int(var_Decenas)) + "D + " + str(int(var_Unidades)) + "U")
elif (len(str(var_Numero)) == 2):
    print(str(int(var_Decenas)) + "D + " + str(int(var_Unidades)) + "U")
elif (len(str(var_Numero)) == 1):
    print(str(int(var_Unidades)) + "U")