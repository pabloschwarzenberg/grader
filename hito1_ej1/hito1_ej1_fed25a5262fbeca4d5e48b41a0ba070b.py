#Nota final

pt=float(input("Ingrese su nota en tareas: "))
pi=float(input("Ingrese su nota en interrogaciones: "))
ne=float(input("Ingrese su nota en examen: "))
pp=float(input("Ingrese su nota en presentacion: "))
pf =(pt*0.3) + (pi*0.3) + (ne*0.3) + (pp*0.1)
print(round(pf,1))