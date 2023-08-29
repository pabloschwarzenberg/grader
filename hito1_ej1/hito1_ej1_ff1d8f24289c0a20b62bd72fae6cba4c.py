#Nota final
PT=eval(input('Ingrese nota de tareas:'))
PI=eval(input('Ingrese nota de interrogaciones:'))
NE=eval(input('Ingrese nota de examenes:'))
PP=eval(input('Ingrese nota de presentación:'))
PF= ((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP))
print(round(PF, 1))     