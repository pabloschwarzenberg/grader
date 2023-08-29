#Nota final
PT= float(input('ingresa nota de tareas: '))
PI= float(input('ingresa nota de interrogaciones: '))
NE= float(input('ingresa nota de examen: '))
PP= float(input('ingresa nota de presentación: '))
       
promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

promediofinal = round(promedio, 1)

print ('El promedio final es: ', promediofinal)