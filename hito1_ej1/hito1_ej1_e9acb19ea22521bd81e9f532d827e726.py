#Nota final
PT = float(input('ingresa nota de tareas: '))
PI = float(input('ingresa nota de interrogaciones: '))
NE = float(input('ingresa nota de examen: '))
PP = float(input('ingresa nota de presentacion: '))

notafinal = PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1
notafinal= round(PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1,1)
print('nota final es: ' , notafinal )

     