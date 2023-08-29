#Nota Final

#PT=  tareas
#PI = interrogaciones
#NE = Examen
#PP = Presentacion

PT = eval(input("Nota de tareas: "))
PI = eval(input("Nota de interrogaciones: "))
NE = eval(input("Nota de examen: "))
PP = eval(input("Nota de presentacion: "))

nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("La Nota Final es: ","{:.1f}".format(nota_final))