#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion

PT = eval(input('porsentaje de tareas: '))
PI = eval(input('porsentaje de interrogaciones: '))
NE = eval(input('porsentaje de examen: '))
PP = eval(input('porsentaje de presentacion: '))

promediofinal=(0.3*PT) + (0.3*PI) + (0.3 * NE) + (0.1*PP)

promediofinal= round(promediofinal,1) 
print('promedio final: ',promediofinal)

    