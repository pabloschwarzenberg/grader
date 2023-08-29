#Nota final
print("hola usuario, por favor ingrese sus notas")
PT= float(input("ingrese el promedio de tareas"))
PI= float(input("ingrese el promedio de interrogaciones"))
NE= float(input("ingrese el promedio del examen"))
PP= float(input("ingrese el promedio de presentaciones"))

R1= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print(round(R1,1))