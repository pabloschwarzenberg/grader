#Nota final
nota1=eval(input('Ingrese la nota de tareas'))
nota2=eval(input('Ingrese la nota de interrogaciones'))
nota3=eval(input('Ingrese la nota de examen'))
nota4=eval(input('Ingrese la nota de presentacion'))

PT = nota1*0.3
PI = nota2*0.3
NE = nota3*0.3
PP = nota4*0.1

promedio = PT+PI+NE+PP

promediofinal = '{0:.1f}'.format(promedio)

print('su promedio es: ',promediofinal)
