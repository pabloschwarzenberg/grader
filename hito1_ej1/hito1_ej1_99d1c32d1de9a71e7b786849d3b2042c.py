PT= float(input("Ingrese su nota de Tareas: "))
PI =float(input("Ingrese su nota de Interrogaciones: "))
NE =float(input("Ingrese su nota de Examenes: "))
PP = float(input("Ingrese su nota de Presentacion: "))

promedio = float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print(round(promedio,1))
