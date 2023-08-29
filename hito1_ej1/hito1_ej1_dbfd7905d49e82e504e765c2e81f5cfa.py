PT = float(input("Ingrese su nota de tareas:"))
PI = float(input("Ingrese su nota de interrogaciones:"))
NE = float(input("Ingrese su nota de examen:"))
PP = float(input("Ingrese su nota de presentacion:"))

Nota_Final = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

Nota_Final = round(Nota_Final,1)

print("Su nota final es", Nota_Final)