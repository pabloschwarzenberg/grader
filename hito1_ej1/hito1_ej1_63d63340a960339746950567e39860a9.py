#Nota final
PT=float(input("ingrese su nota de tareas: "))
PI=float(input("ingrese su nota de presentacion: "))
NE=float(input("ingrese su nota de examen: "))
PP=float(input("ingrese su nota de interrogacion: "))

resultado = (((0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)*10)//1)/10
print(resultado)