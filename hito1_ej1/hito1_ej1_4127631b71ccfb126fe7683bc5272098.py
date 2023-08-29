#Nota final
print("Calculo Promedio Final")
pt = float(input("ingresa promedio de notas de tareas: "))
pi = float(input("ingresa promedio de notas de interrogaciones: "))
ne = float(input("ingresa nota de examen: "))
pp = float(input("ingresa nota de presentacion: "))
calculo = (0.3 * pt)+ (0.3*pi)+(0.3*ne)+(0.1*pp)
calculoround = round(calculo,1)
print ("Promedio final:",calculoround)