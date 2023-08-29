#Nota final
PT=eval(input("nota de tares"))
PI=eval(input("nota de interrogaciones"))
NE=eval(input("notas de examen"))
PP=eval(input("notas de presentacion"))

promedio=0.3*PT+0.3*PI+0.3*NE+0.1*PP
print("promedio final es:",round(promedio,1))