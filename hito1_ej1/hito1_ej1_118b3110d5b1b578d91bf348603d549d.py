#Nota final
pt = float(input("Ingrese las notas de las tareas:"))
pi = float(input("Ingrese las notas de las interrogaciones:"))
ne = float(input("Ingrese las notas del exámen:"))
pp = float(input("Ingrese las notas de la presentación:"))  
pf = 0.3*pt+0.3*pi+0.3*ne+0.1*pp
print("El promedio final es:",round(pf,1))