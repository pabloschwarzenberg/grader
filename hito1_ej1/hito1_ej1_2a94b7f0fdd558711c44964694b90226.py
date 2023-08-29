#Nota final
PT= float(input("inserta la nota de tares:"))
PI= float(input("inserta la nota de interrogaciones:"))
NE= float(input("inserta la nota de examen:"))
PP= float(input("inserta la nota de presentacion:"))
Z= (0.3 * PT) + (0.3 *PI) + (0.3 * NE) + (0.1 * PP)
Z2= round(Z,1)
print("el promedio es:",Z2)