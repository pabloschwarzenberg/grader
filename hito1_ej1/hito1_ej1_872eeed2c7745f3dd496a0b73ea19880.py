#Nota final
PT=input("inserte su promedio en tareas:")

PT=float(PT)

PI=input("inserte su promedio en interrogaciones:")

PI=float(PI)

NE=input("inserte su nota de examen:")

NE=float(NE)

PP=input("inserte su notade presentacíon:")

PP=float(PP)



prom=(0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

prom=round(prom,1)
print(prom)
      