#Nota final
PT=eval(input("ingrese su nota en tareas: "))
PI=eval(input("ingrese su nota en interrogaciones: "))
NE=eval(input("ingrese su nota en examen: "))
PP=eval(input("ingrese su nota de presentacion: "))
mulpt=0.3*PT
mulpi=0.3*PI
mulne=0.3*NE
mulpp=0.1*PP
suma=mulpt+mulpi+mulne+mulpp
print(suma)