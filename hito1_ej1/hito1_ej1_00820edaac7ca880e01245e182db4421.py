#Nota final
#Entrada
print("El promedio final del ramo")
      
pt= float(input("ingrse la nota de trabajos: "))
pi= float(input("Ingrese las notas de sus interrogaciones: "))
ne= float(input("Ingrese la nota del examen: "))
pp= float(input("Ingrese la nota de presentacion: "))


promedio = (0.3*pi)+(0.3*ne)+(0.3*pt)+(0.1*pp)
promedio = round(promedio, 1)

print("su promedio es de: -----> ", promedio)