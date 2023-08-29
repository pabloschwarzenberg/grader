#Nota final
PT = float(input("ingrese su nota de tareas: "))
PI = float(input("ingrese su nota de interrogantes: "))
NE = float(input("ingrese su nota de Examen: "))
PP = float(input("ingrese su nota de Presentacion: "))

PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print("su primedio final es: %.1f " %(PF))