pt = float(input("Ingrese el promedio de notas de sus tareas: "))
pi = float(input("Ingrese el promedio de notas de sus interrogaciones: "))
ne = float(input("Ingrese la nota de su examen: "))
pp = float(input("Ingrese la nota de su prosentación: "))
pf = float((pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1))
if pf <=7:
    round(pf)
    print("Su promedio final es {:0.1f}".format(pf))