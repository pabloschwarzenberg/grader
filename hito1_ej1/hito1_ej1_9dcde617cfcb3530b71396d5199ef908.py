#Nota final
print("Bienvenido a Huevito rey calculador de nota final")
PT= eval(input("Ingrese la nota de la tarea "))
PI= eval(input("Ingrese la nota de interrogaciones "))
NE= eval(input("Ingrese la nota del examen "))
PP= eval(input("Ingrese la nota de presentacion "))
NY= PT+PI+NE
p_f= (NY*0.3) + (PP*0.1)
print(round(p_f,1))