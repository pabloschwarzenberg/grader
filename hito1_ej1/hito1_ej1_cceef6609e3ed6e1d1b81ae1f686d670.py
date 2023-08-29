#Nota final
PT = float(input("ingresar la nota de las tareas: "))
PI = float(input("ingresar la nota de las interrogaciones: "))
NE = float(input("ingresar la nota de el examen: "))
PP = float(input("ingresar la nota de la presentación: "))
  
p = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 2)
print("el promedio final es: ", p)