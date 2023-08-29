#Nota final
pt= float(input("ingrese su promedio obtenido en tareas : "  ))
pi= float(input("ingrese su promedio obtenido en interrogaciones : "  ) )
ne= float(input("ingrese su promedio obtenido en examen : " ) )
pp= float(input("ingrese su promedio obtenido en presentacion : "  ) )

#Los porcentajes
t= (0,3 * pt)
i= (0.3 * pi)
n= (0.3 * ne)
p= (0,1 * pp)

pf= ( pt + pi + ne + pp)//4

print(" su promedio final es : " ,pf  )