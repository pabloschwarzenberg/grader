#Nota final

PT = float(input("Ingresar nota de tareas: "))
PI = float(input("Ingresar nota de interrogaciones: "))
NE = float(input("Ingresar nota de exámen: "))
PP = float(input("Ingresar nota de presentación: "))
      
PF = round((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP), 1)
      
print(PF)