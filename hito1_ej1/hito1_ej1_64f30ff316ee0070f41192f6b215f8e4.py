##PT = Tareas
##PI = Interrogaciones
##NE =  Examen
##PP = Presentacion
##0.3PT + 0.3PI + 0.3NE + 0.1PP

Nota_T=eval(input("Ingresa Nota de Tareas: "))
Nota_I=eval(input("Ingresa Nota de Interrogaciones: "))
Nota_E=eval(input("Ingresa Nota de Examen: "))
Nota_P=eval(input("Ingresa Nota de Presentacion: "))
Nota_Final=Nota_T*0.3+Nota_I*0.3+Nota_E*0.3+Nota_P*0.1

print ('Nota Final es:',round(Nota_Final,1))
      