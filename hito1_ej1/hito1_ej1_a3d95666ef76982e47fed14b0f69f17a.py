#Nota final
PT = float(input("Ingrese nota tarea:"))
while PT > 7 or PT < 1:
    print("Nota fuera de rango")
    PT = float(input("Ingrese nota tarea:"))

PI = float(input("ingrese nota de interrogacion:"))
while PI > 7 or PI < 1:
    print("Nota fuera de rango")
    PI = float(input("Ingrese nota interrogacion:"))

NE = float(input("Ingrese nota examen:"))
while NE > 7 or NE < 1:
    print("Nota fuera de rango")
    NE = float(input("Ingrese nota examen:"))

PP = float(input("Ingrese nota presentacion:"))
while PP > 7 or PP < 1:
    print("Nota fuera de rango")
    PP = float(input("Ingrese nota presentacion:"))
  
promedio= round((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP),1)
print(promedio)      