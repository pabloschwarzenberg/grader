#Nota Final
#Encabezado
print('Calcular nota final')
#Definir variables y solicitar info
PT = float(input('Ingresar nota de "Tareas": '))
PI = float(input('Ingresar nota de "Interrogantes": '))
NE = float(input('Ingresar nota de "Examen": '))
PP = float(input('Ingresar nota de "Presentación": '))
#Desarrollo
NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
#Resultado
print('Tu nota final es: ', round(NF , 1))
print('FIN.')
#Nota final
      