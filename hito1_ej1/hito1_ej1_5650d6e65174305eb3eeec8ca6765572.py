PT=eval(input('Ingresa la nota de tu tarea:'))
PI=eval(input('Ingresa la nota de tu interrogacion:'))
NE=eval(input('Ingresa la nota de tu examen:'))
PP=eval(input('Ingresa la nota de tu presentacion:'))

promedio=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print('Tu promedio final es:',round(promedio,1))
      