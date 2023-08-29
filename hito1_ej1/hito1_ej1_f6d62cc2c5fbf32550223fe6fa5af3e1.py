print("ingrese sus cuatros notas")
PT=float(input("ingrese su nota de tareas es de: "))
PI=float(input("ingrese su nota de interrogacion es: "))
NE=float(input("ingrese su nota de examen es de: "))
PP=float(input("ingrese su nota de presentacion es de: "))
N=((0.3*PT+0.3*PI+0.3*NE+0.1*PP))
N=round(N,1)
print("el promedio redondeado a un decimal es:",N)
      