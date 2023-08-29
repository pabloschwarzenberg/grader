#Nota final
PT=float(input("ingrese su nota final de las tareas:"))
PI=float(input("ingrese su nota final de las interrogaciones:"))
NE=float(input("ingrese su nota final del examen:"))
PP=float(input("ingrese su nota final de presentacion:"))
NF=round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1)
print("su promedio final es:",NF)