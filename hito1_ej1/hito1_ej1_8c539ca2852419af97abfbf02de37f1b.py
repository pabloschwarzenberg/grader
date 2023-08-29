PT=float(input('Ingrese su nota TAREAS : '))
PI=float(input('Ingrese su nota INTERROGANTES : '))
NE=float(input('Ingrese su nota EXAMEN : '))
PP=float(input('Ingrese su nota PRESENTACION : '))

promedio= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
#"{:.10f}".format(10/3)
promedio="{:.1f}".format(promedio)
print(promedio)