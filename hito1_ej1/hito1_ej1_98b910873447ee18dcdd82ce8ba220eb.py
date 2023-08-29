#Nota final
PT= tareas= float(input("ingresa la nota de tus tareas:"))    
PI= interrogantes= float(input("ingresa la nota de tus interrogantes:"))
NE= examen= float(input("ingrese la nots de tu examen:"))
PP= Presentacion= float(input("ingrese la nota de presentacion:"))
Nota_final= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("su nota final es:", round(Nota_final,1))      