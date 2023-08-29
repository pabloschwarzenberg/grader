pt= float(input("Ingresa nota Tareas"))
pi= float(input("Ingresa nota Interrogaciones"))
ne= float(input("Ingresa nota Examen"))
pp= float(input("Ingresa nota Presentacion"))


promedio_final= 0.3*pt+0.3*pi+0.3*ne+0.1*pp


redondeado= round(promedio_final,1)
print(redondeado)