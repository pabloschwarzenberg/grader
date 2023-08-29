#Nota final
PT=float(input("ingrese nota tarea  : "))
PI=float(input("ingrese nota interrogaciones  : "))
NE=float(input("ingrese nota examen  : "))
PP=float(input("ingrese nota presentación   : "))
resultado=0.3*PT+0.3*PI+0.3*NE+0.1*PP
resultado = round(float(resultado),1)
print("tu promedio final es",resultado)