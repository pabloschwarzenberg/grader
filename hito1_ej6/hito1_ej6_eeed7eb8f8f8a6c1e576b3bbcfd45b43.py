#Ordenar tres números
var_Num1 = int(input("Ingrese un número entero al azar: "))
var_Num2 = int(input("Ingrese otro número entero al azar: "))
var_Num3 = int(input("Ingrese un último número entero al azar: "))
var_Min = min(var_Num1, var_Num2, var_Num3)
var_Max = max(var_Num1, var_Num2, var_Num3)
var_Med = (var_Num1 + var_Num2 + var_Num3) - (var_Min + var_Max)
print(str(var_Min) + ", " + str(var_Med) + ", " + str(var_Max))