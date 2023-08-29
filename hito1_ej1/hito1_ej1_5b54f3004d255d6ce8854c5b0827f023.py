#Nota final
      
pt = eval(input("Ingrese la nota de tareas: "))
pi = eval(input("Ingrese la nita de interrogaciones: "))
ne = eval(input("Ingrese la nota de examen: "))
pp = eval(input("Ingrese la nota de presentacion: "))

prom = 0.3*(pt) + 0.3*(pi) + 0.3*(ne) + 0.1*(pp)

print("El promedio final es: ",round(prom,1))