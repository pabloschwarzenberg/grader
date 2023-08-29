#Nota final
PT = eval(input('Ingresa nota de Tareas: '))
PI = eval(input('Ingresa nota de Interrogaciones: '))
NE = eval(input('Ingresa nota de Examen: '))
PP = eval(input('Ingresa nota de Presentación: '))

Notafinal = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 1)

print('Tu Nota Final es: ' , Notafinal)
      