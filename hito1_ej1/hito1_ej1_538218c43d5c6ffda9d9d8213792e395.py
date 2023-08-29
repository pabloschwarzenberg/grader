#Nota final
print('Ingrese sus notas')
print('Recordatorio: Sun notas deben estar entre 1.0 y 7.0')
t= eval(input('Ingrese la nota de tareas: '))
i= eval(input('Ingrese la nota de interrogaciones: '))
e= eval(input('Ingrese la nota del examen: ')) 
p= eval(input('Ingrese la nota de la presentación: '))

f= t*0.3 + i*0.3 + e*0.3 + p*0.1

if 1<=t<=7 and 1<=i<=7 and 1<=e<=7 and 1<=p<=7:
    print('Su nota final es: ',round(f ,1))
else:
    print('acuerdese de digitar sun notas entre 1.0 y 7.0')    