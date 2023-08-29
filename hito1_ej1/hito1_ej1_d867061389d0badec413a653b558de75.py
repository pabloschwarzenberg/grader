#Nota final
input("Por favor la nota ingrésela con (.) y NO con (,), ejemplo: 5.4")
PT=float(input("Ingrese su nota del promedio de las Tareas: "))
PI=float(input("Ingrese su nota del promedio las Interrogaciones: "))
NE=float(input("Ingrese su nota del examen: "))
PP=float(input("Ingrese su nota de presentación: "))
print("Su promedio final es:",round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1))