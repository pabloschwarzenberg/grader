#Cálculo del dígito verificador de un rut
var_Rut = int(input("Ingrese un número para obtener su DV: "))
var_DV = int()
var_Sumatoria = int()
var_Multiplica = 2
for item in reversed(str(var_Rut)):
    if var_Multiplica > 7:
        var_Multiplica = 2
    var_Sumatoria += int(item) * var_Multiplica
    var_Multiplica += 1
var_Mod11 = (var_Sumatoria % 11)
var_PreDV = 11 - var_Mod11
if var_PreDV == 11:
    var_DV = 0
elif var_PreDV == 10:
    var_DV = "k"
else:
    var_DV = var_PreDV
print("dv=" + str(var_DV))