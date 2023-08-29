#Nota final
PT = eval(input("ingrese nota de tareas: "))
PI = eval(input("ingrese nota de interrogaciones: "))
NE = eval(input("ingrese nota de examen: "))
PP = eval(input("ingrese nota de presentacion: "))
#calculamos la suma, y la guardamos en la variable (promedio)
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
#mostrar resultado
print("el resultado es: ",promedio)     