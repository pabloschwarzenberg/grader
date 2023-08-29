NT = eval(input("Tareas: "))
NI = eval(input("Interrogaciones: "))
NE = eval(input("Examen: "))
NP = eval(input("Presentacion: "))

prom = (round(0.3*NT + 0.3*NI + 0.3*NE + 0.3*NP))

print("su promedio es: ",round(prom))
