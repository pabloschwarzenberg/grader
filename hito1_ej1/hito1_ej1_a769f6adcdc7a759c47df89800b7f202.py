#Nota final
PT = eval(input('Ingrese su nota de Tareas: '))      
PI = eval(input('Ingrese su nota de Interrogaciones: '))
NE = eval(input('Ingrese su nota de Examen: '))
PP = eval(input('Ingrese su nota de Presentacion: '))

PT = 0.3*PT
PI = 0.3*PI
NE = 0.3*NE
PP = 0.1*PP

#PT = (PT//1000)
#PI = (PI//1000)
#NE = (NE//1000)
#PP = (PP//1000)

suma = PT+PI+NE+PP
print('Resultado: ',suma)