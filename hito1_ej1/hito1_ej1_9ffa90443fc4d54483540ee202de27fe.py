#Nota final
PT = float(input("Ingrese su nota de tareas porfavor: "))
PI = float(input("Ingrese su nota de interrogaciones porfavor: "))
NE = float(input("Ingrese su nota de examen porfavor: "))
PP = float(input("Ingrese su nota de presentacion porfavor: "))
PF = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
print ("Promedio final es: ", round(PF, 1),"!")