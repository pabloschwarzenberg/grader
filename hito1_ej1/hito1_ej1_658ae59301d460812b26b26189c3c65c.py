#Nota final
pt = eval(input("Ingrese la nota de las tareas:"))
pi = eval(input("Ingrese la nota de las interrogaciones:"))
ne = eval(input("Ingrese la nota del examen"))
pp = eval(input("Ingrese la nota de la presentacion"))
formula = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
print("El resultado redondeado a un decimal es:" , formula)