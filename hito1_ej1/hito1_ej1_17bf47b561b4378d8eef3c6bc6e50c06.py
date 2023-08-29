#Nota final
PT = eval(input("Ingrese la nota de la tarea: "))
PI = eval(input("Ingrese la nota de la interrogaciones: "))
NE = eval(input("Ingrese la nota de la Examen: "))
PP = eval(input("Ingrese la nota de presentacion: "))
Ta = PT * 0.3
In = PI * 0.3
Ex = NE * 0.3
Pr = PP * 0.1
suma = Ta + In + Ex + Pr
aprox = round(suma)
print("Nota final {:.1f}".format(suma))