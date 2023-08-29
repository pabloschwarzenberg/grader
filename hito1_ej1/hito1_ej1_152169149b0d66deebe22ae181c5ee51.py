pt = float(input("ingrese su nota en tareas: "))
pi = float(input("ingrese su nota en floaterrogaciones: "))
ne = float(input("ingrese su nota en examen: "))
pp = float(input("ingrese su nota en presentacion: "))

promedio = pt * 0.3 + pi * 0.3 + ne * 0.3 + pp * 0.1
promedio = '%.1f' % round(promedio)
print(promedio)