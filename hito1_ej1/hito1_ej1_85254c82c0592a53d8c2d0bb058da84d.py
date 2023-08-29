#Nota final
PT=eval(input('Ingresa nota de Tareas:'))
PI=eval(input('Ingresa nota de Interrograciones:'))
NE=eval(input('Ingresa nota de Examen:'))
PP=eval(input('Ingresa nota de Presentación:'))
PF=((3/10)*PT)+((3/10)*PI)+((3/10)*NE)+((1/10)*PP)
PF=round(PF,1)
print('Tu promedio final:',PF,)    