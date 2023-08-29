#Nota final
PT=float(input("Ingresa la nota de puntaje de tus tareas "))
PI=float(input("ingresa tu nota de interrogaciones "))
NE=float(input("Ingresa tu nota del examen "))
PP=float(input("ingresa tu nota por presentación "))
promedio=(PT*0.3+PI*0.3+NE*0.3+PP*0.1)
print("el promedio es ", round(promedio,1))