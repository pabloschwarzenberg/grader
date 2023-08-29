pt= float(input("tareas: "))
pi= float(input("interrogaciones: "))
ne= float(input("nota examen: "))
pp= float(input("presentacion: "))

resultado = (0.3*pt+0.3*pi+0.3*ne+0.1*pp)

redondeado = round(resultado, 1)

print(resultado)