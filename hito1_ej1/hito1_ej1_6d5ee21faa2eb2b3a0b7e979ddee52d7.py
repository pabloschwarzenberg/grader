#Nota final
pt = eval(input("ingrese nota de tarea:"))
pi = eval(input("ingrese  nota de interrogaciones:"))
ne = eval(input("ingrese nota del examen:"))
pp = eval(input("ingrese nota de  presentación:"))

promedio = pt * 0.3 + pi * 0.3 + ne * 0.3 + pp * 0.1
print("su promedio es :",round(promedio,1))      