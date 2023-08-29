#Nota final
PT = float(input("Introduzca su nota de tareas: "))
PI = float(input("Introduzca su nota de interrogaciones: "))
NE= float(input("Introduzca su nota de examen: "))
PP =float(input("Introduzca su nota de presentación: "))
promedio= float (0.3*PT+0.3*PI+0.3*NE+0.1*PP)
notafinal= round (promedio,1)
print ("Su nota final es: ", notafinal)