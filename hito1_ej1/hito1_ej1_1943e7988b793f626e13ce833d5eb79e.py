#Nota final
num= [float(input('ingrese nota tareas: ')), float(input('ingrese nota interrogaciones: ')), float(input('ingrese Examen: ')), float(input('ingrese nota presentacion: '))]
print(round(0.3*(num[0]+num[1]+num[2])+0.1*num[3],1))      