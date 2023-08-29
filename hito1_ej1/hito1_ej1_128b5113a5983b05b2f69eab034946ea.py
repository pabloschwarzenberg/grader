#jeannetteaguilera
print("promedio de notas")
PT=float(input("ingresa el promedio de notas de tus tareas(PT)"))
PI=float(input("ingresa el promedio de notas de las interrogaciones(PI)"))
NE=float(input("ingresa tu nota de examen(NE) "))
PP=float(input("ingresa la nota de la presentacion (PP)"))
f=(0.3*PT)+(0.3*NE)+(0.1*PP)+(0.3*PI)
print("su promedio de nota es",round(f,1))