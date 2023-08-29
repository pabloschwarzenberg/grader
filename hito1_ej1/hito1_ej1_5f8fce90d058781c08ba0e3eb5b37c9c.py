print("ingrese las notas de: ")
PT=float(input("tareas: "))
PI=float(input("interrogaciones: "))
NE=float(input("examen: "))
PP=float(input("presentacion: "))
x=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
round(x,1)
print("promedio final",x)
      