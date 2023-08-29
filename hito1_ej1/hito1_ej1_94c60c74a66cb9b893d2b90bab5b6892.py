#ejercicio de sacar nota final
#PT=tareas
#PI=interrogaciones
#NE=examen
#PP=presentacion
PT=float(input("ingrese nota de tareas: "))
PI=float(input("ingrese nota de interrogaciones "))
NE=float(input("ingrese nota de examen "))
PP=float(input("ingrese nota de presentacion "))
prom=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("el promedio final es: ","{:.1f}".format(prom))
      