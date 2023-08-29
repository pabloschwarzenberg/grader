#Nota final
pt = eval(input("ingrese nota de tareas:"))
pi = eval(input("ingrese nota de interrogaciones:"))
ne = eval(input("ingrese nota examen:"))
pp = eval(input("ingrese presentacion:"))
nota_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
print("la nota final es", nota_final)     