#Nota final
      
pt = eval(input("Ingrese la nota de sus tareas: "))

pi = eval(input("Ingrese la nota de sus interrogaciones: "))

ne = eval(input("Ingrese la nota de su examen: "))

pp = eval(input("Ingrese la nota de su presentación: "))

nf = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
nf = round(nf,1)

print("Su nota final es: ",nf)
