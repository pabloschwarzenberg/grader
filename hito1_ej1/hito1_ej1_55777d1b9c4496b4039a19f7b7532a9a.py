#Nota final
print("introduce la primera nota")
PT=input("ingrse nota de tarea : ")
print("introduce la primera nota")
PI=input("ingrse nota de interrogaciones : ")
print("introduce la primera nota")
NE=input("ingrse nota de examen : ")
print("introduce la primera nota")
PP=input("ingrse nota de presentacion : ")

PT=float(PT)
PI=float(PI)
NE=float(NE)
PP=float(PP)

#calcular el promedio 
promedio=round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1)
print(promedio)

                 