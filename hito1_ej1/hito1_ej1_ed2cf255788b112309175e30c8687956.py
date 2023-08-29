#Nota final
PT=float(input("que nota tuviste en la tarea? "))
PI=float(input("y la nota de interrogaciones? "))
NE=float(input("y la del examen? "))
PP=float(input("y la presentacion? "))
final=round((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP),1)
print ("tu promedio final es", final)