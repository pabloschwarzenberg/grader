#Nota final
#ingresar variables
notat = eval(input("Ingrese nota de tareas: "))
notai = eval(input("Ingrese nota de la interrogacion: "))
notae = eval(input("Ingrese nota del examen: "))
notap = eval(input("Ingrese nota de presentacion: "))
#realizar resulatados de nota final
nota = 0.3*notat+0.3*notai+0.3*notae+0.1*notap
#mostrar nota final
print("Tu nota final es ", nota)      