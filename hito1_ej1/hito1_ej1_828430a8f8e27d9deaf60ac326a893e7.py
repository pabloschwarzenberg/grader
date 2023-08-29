#Nota final
PT=eval(input('ingrese nota de tarea:'))
PI=eval(input('ingrese nota de interrogaciones:'))
NE=eval(input('ingrese nota de examenes:'))
PP=eval(input('ingrese nota de presentacion:'))
PF= (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
print(round(PF, 1))
