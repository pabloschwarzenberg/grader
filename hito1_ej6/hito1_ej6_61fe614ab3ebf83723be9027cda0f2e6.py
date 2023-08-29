#Ordenar tres números
variable_1 = int(input("Ingrese un numero:"))
variable_2 = int(input("Ingrese un numero:"))
variable_3 = int(input("Ingrese un numero:"))

cal_1 = min(variable_1, variable_2, variable_3)
cal_3 = max(variable_1, variable_2, variable_3)
cal_2 = (variable_1 + variable_2 + variable_3) - cal_1 - cal_3

print("Los numeros ordenados de menor a mayor seria:", cal_1, cal_2, cal_3)