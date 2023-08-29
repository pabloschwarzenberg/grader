#Nota final
  
PT = float(input("ingrese Tareas : " ))
PI = float(input("ingrese Interrogaciones : " ))
NE = float(input("ingrese Examen : " ))
PP = float(input("ingrese Presentacion : " ))
Promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print('Promedio Final:',"{:.1f}".format(Promedio))    