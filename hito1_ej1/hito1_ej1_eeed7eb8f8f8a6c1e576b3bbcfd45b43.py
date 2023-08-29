#Nota final
var_PT = float(input("Ingrese nota de tareas: "))
var_PI = float(input("Ingrese nota de interrogaciones: "))
var_NE = float(input("Ingrese nota del exámen: "))
var_PP = float(input("Ingrese nota de presentación: "))
var_PromedioFinal = (0.3 * var_PT) + (0.3 * var_PI) + (0.3 * var_NE) + (0.1 * var_PP)
print(round(var_PromedioFinal, 1))