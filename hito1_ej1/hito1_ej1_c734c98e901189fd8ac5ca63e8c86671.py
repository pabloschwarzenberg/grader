#Nota final
pt=eval(input('Ingrese nota de tareas.'))
pi=eval(input('Ingrese nota de interrogaciones'))
ne=eval(input('Ingrese nota de examen'))
pp=eval(input('Ingrese nota de presentacion'))


pa=pt*0.3
pb=pi*0.3
pc=ne*0.3
pd=pp*0.1
pe=pa+pb+pc+pd

print('La nota final es:',pe)