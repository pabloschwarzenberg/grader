#Nota final
tareas = float(input('escriba el numero 1: '))
interrogacion = float(input('escriba el numero 1: '))
examen = float(input('escriba el numero 2: '))
presentacion = float(input('escriba el numero 3: '))

res = 0.3*tareas+0.3*interrogacion+0.3*examen+0.1*presentacion
res = round(res,1)
print(res)