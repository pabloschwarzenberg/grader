PT = float(input('Ingrese la nota de las tareas: '))
PI = float(input('Ingrese la nota de la interrogación: '))
NE = float(input('Ingrese l anota de el examenen: '))
PP = float(input('Ingrese la nota de la presentación: '))

Formula = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP


print('La nota filna es: ',round(Formula,1))
