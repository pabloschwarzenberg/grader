#Nota final
PT=float(input("ingrese la nota de tarea  : "))
PI=float(input("ingrese las nota de las interrogaciones  : "))
NE=float(input("ingrese la nota del examen  : "))
PP=float(input("ingrese la nota de presentación   : "))
resultado=0.3*PT+0.3*PI+0.3*NE+0.1*PP
resultado = round(float(resultado),1)
print("tu promedio final es",resultado)    