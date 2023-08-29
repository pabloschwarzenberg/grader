#Nota final
PT = float(input('Ingrese la nota de la tarea: ' ))
PI = float(input('Ingrese la nota de interrogaciones: ' ))
NE = float(input('Ingrese la nota de la examen: ' ))
PP = float(input('Ingrese la nota de la presentacion: ' ))
PF = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
P_R = round(PF, 1)
PF_R = print('El promedio final es de: ',P_R)