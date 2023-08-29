#Nota final
PT = float(input("Ingresu su nota de tareas: "))
PI = float(input("Ingrese su nota de interrogaciones: "))
NE = float(input("Ingrese su nota de examen: "))
PP = float(input("Ingrese su nota de presentacion: "))
if PT>=1 and PI>=1 and NE>=1 and PP >=1:
    calculo = round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1)
    print(f"su nota resultante es: {calculo}")
else:
    print("Corrija sus notas, tienen que ser mayoe o igual a 1.0")