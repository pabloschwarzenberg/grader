#Nota final
pt = float(input("Ingrese la nota de Tareas: "))      
pi = float(input("Ingrese la nota de Interrogaciones: "))      
ne = float(input("Ingrese la nota de Examen: "))      
pp = float(input("Ingrese la nota de Presentacion: "))      

pt = (pt * 0.3)
pi = (pi * 0.3)
ne = (ne * 0.3)
pp = (pp * 0.1)

promedio = (pt + pi + ne + pp)
print(round(promedio,1))



