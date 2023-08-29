PT=float(input("ingrese nota de la tarea  : "))
PI=float(input("ingrese nota de la interrogaciones  : "))
NE=float(input("ingrese nota de la examen  : "))
PP=float(input("ingrese nota de la presentación   : "))
resultado=0.3*PT+0.3*PI+0.3*NE+0.1*PP
resultado = round(float(resultado),1)
print("tu promedio final es",resultado)