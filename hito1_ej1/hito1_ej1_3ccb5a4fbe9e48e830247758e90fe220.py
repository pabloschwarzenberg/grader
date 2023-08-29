#Nota final
a = eval(input('Nota tareas: '))
b = eval(input('Nota interrogaciones: '))
c = eval(input('Nota examen: '))
d = eval(input('Nota presentacion: '))
if 0.3*a+0.3*b+0.3*c+0.1*d < 0 :
  print('el valor es decimal')
else: 
  print('Nota final = ',(0.3*a+0.3*b+0.3*c+0.1*d))