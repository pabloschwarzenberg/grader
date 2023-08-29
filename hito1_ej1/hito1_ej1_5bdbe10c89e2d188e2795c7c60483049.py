#Nota final
print("Ingrese sus notas")
a=eval(input("Nota de tareas:"))
b=eval(input("Nota de interrogaciones:"))
c=eval(input("Nota examen:"))
d=eval(input("Nota de presentacion:"))

f= round(0.3*a + 0.3*b + 0.3*c + 0.1*d, 1)
print("su nota final es:", f)
