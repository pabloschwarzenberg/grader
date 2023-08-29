#Nota final
def promedio():
    pt = float(input("Nota Tareas: "))
    pi = float(input("Nota Interrogaciones: "))
    ne = float(input("Nota Examenes: "))
    pp = float(input("Nota presentación: "))
    pro = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
    red = round(pro ,1)
    return red

print(promedio())      