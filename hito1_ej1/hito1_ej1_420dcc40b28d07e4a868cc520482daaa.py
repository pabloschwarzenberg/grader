pt= float(input("ingresa nota tareas"))
pi= float(input("ingresa nota interrogaciones"))
ne= float(input("ingresa nota examen"))
pp= float(input("ingresa nota presentacion"))


promedio_final= 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp


redondeado= round(promedio_final,1)
print(redondeado)
      