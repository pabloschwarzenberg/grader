#Nota final
t = eval(input("Nota Tareas: "))
i = eval(input("Nota interrogaciones: "))
e = eval(input("Nota Examen: "))
p = eval(input("Nota presentación: "))

pf = (0.3 * t) + (0.3 * i) + (0.3 * e) + (0.1 * p)

print("El promedio final es ", round(pf,1))