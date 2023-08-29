#Nota Final
t=float(input("ingresa tu nota de tareas: "))
i=float(input("ingresa tu nota de interrogaciones: "))
e=float(input("ingresa tu nota de examen: "))
p=float(input("ingresa tu nota de presentacion: "))


f=(0.3*t)+(0.3*i)+(0.3*e)+(0.1*p)
x=round(f,1)

print("tu promedio final es: ",x)