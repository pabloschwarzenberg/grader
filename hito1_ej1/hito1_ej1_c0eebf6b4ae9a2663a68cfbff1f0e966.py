#Nota final
PT = float(input("Ingrese su nota final de notas -> "))
PI = float(input("Ingrese su nota final de interrogaciones -> "))
NE = float(input("Ingrese su nota final de examen -> "))
PP = float(input("Ingrese su nota final de presentaciones -> "))

promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
Nota = round(promedio_final,1)
print(Nota)