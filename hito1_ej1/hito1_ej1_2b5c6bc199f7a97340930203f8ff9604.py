#Nota final
PT= float(input("Ingrese su nota de tareas: "))
PI= float(input("Ingrese su nota de interrogaciones: "))
NE= float(input("Ingrese su nota de examen: "))
PP= float(input("Ingrese su nota de presentación: "))
promedio= PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1
print("El promedio de notas final es: ", round(promedio,1))      