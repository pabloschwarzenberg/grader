PT=float(input("Ingresar nota de las tareas: "))
PI=float(input("Ingresar nota de las interrogaciones: "))
NE=float(input("Ingresar nota de los examenes: "))
PP=float(input("Ingresar nota de las presentaciones"))
NT= (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)%4
round(NT,1)
print(NT)