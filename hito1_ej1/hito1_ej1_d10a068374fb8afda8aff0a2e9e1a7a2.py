pt = (float(input("ingresar notas tareas ")))

pi = (float(input("ingresar notas interrogaciones ")))

ne = (float(input("ingresar notas Examen ")))

pp = (float(input("ingresar notas Presentacion ")))

nota=round((0.3*pt+0.3*pi+0.3*ne+0.1*pp),1)
print("el resultado de todo es ", nota)