#Nota final
PT = float(input('ingrese su nota de tareas'))
PI = float(input('ingrese su nota de interrogaciones'))
NE = float(input('ingrese su nota de examenes'))
PP = float(input('ingrese su nota presentacion'))
Nota_Final = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print(round(Nota_Final, 1))