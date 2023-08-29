#Nota final
PT= eval(input('Ingrese su puntaje de tareas: '))
PI= eval(input('Ingrese su puntaje de interrogaciones: '))
NE= eval(input('Ingrese su puntaje de examenes: '))
PP= eval(input('Ingrese su puntaje de presentaciones: '))

suma= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print('Nota final: ', round(suma, 1))     