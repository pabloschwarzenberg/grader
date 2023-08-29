
PT = float(input("inserte notas promediadas de tareas: "))
PI = float(input("inserte notas promediadas de interrogaciones: "))
NE = float(input("inserte nota promediadas de examenes: "))
PP = float(input("inserte nota promediada de presentaciones: "))
calculo_de_la_nota_de_presentacion = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
x = calculo_de_la_nota_de_presentacion
print("calculo de la nota de prensentacion:  ", round(x,1))