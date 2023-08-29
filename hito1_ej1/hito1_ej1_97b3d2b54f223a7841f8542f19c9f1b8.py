#Nota final
a= float(input("Ingrese nota de tareas: "))
b= float(input("Ingrese nota de interrogaciones: "))
c= float(input("Ingrese nota de exmane: "))
d= float(input("Ingrese nota de presentacion: "))
r= 0.3*a + 0.3*b + 0.3*c + 0.1*d

print("El promedio final es {:.1f}".format(r))      