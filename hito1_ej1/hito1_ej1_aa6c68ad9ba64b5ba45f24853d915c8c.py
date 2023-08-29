#Nota final
pt= float(input("su nota de tareas es de: "))
pi= float(input("su nota en interrogaciones es de: "))
ne= float(input("su nota de examenes es de: "))
pp= float(input("su nota de presentaciones es de: "))
promedio_final= ((0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp))
promedio_final= round(promedio_final,1)
print("promedio redondeado es: ", promedio_final)

