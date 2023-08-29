#Nota final
print("pt = tareas")
print("pi = interrogaciones")
print("ne = examen")
print("pp = presentacion")

pt = float(input("ingrese nota pt: "))
pi = float(input("ingrese nota pi: "))
ne = float(input("ingrese nota ne: "))
pp = float(input("ingrese nota pp: "))

formula = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print("su nota final es: ",round(formula,1))