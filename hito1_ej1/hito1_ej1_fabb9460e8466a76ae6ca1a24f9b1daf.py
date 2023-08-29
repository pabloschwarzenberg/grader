#Nota final
      #Gustavo Altez irarrazabal
NT=eval(input("ingrese su calificacion de tareas: "))
NI=eval(input("ingrese su calificacion de interrogaciones: "))
NE=eval(input("ingrese su calificacion del Examen: "))
NP=eval(input("ingrese su calificion de la presentacion: "))
Promedio=((0.3*NT)+(0.3*NI)+(0.3*NE)+(0.1*NP))
print("Su Promedio es: ", round(Promedio,1))