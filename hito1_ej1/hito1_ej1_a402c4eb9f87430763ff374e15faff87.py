#Nota final
print ("Ingrese 4 notas")
PT = float(input("Ingrese su nota de tareas "))
PI = float(input("Ingrese su nota de interrogaciones "))
NE = float(input("Ingrese su nota de examen "))
PP = float(input("Ingrese su nota de presentación "))
calculo_promedio = 0.3 * PT + 0.3 * PI + 0.3 *NE + 0.1 * PP
promedio = round(calculo_promedio,2)
print ("De menor a mayor el orden es ", promedio)