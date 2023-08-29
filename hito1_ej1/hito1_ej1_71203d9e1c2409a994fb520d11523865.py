#Nota final
pt = float(input("ingrese su nota de tareas: "))
pi = float(input("ingrese su nota de interrogacion: "))
ne = float(input("ingrese su nota de examen: "))
pp = float(input("ingrese su nota de presentacion: "))
notafinal=(0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp)
nota_final=round(notafinal)
print("tu nota final es: ", notafinal)