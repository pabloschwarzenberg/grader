#Nota final
print("PT = TAREAS")
print("PI = INTERROGACIONES")
print("NE = EXÁMEN")
print("PP = PRESENTACIÓN")
print("PF = PROMEDIO")

PT = float(input("Ingrese su nota de PT:  "))
PI = float(input("Ingrese su nota de PI:  "))
NE = float(input("Ingrese su nota de NE:  "))
PP = float(input("Ingrese su nota de PP:  "))

PF = (0.3 * (PT) + 0.3 * (PI) + 0.3 * (NE) + 0.1 * (PP))
print("Su promedio final es:  ")
print (round(PF, 1))   