#Nota final
PT=float(input("Ingrese nota de la tarea:"))
PI=float(input("Ingrese nota de las Interrogaciones:"))
NE=float(input("Ingrese nota del Examen:"))
PP=float(input("Ingrese nota de la presentación:"))

P=(0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)

p= round(P, 1)

print("Este es tu promedio de Notas owo:", p)      