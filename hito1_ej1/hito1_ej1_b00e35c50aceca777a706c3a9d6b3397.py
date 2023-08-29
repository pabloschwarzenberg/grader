##ingrese notas

PT=int(input("ingrese nota Tarea: "))
PI=int(input("ingrese nota Interrogaciones: "))
NE=int(input("ingrese nota Examen: "))
PP=int(input("ingrese nota Presentación: "))

##Calculo promedio
promedio=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
#{:.10f}".format(10/3)
promedio="{:.1f}".format(promedio)
print(promedio)