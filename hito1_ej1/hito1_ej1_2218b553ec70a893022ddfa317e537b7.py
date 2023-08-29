#Nota final
T = float(input("Ingresa tu nota en las tareas: "))
I = float(input("Ingresa tu nota de las interrogaciones: "))
E = float(input("Ingresa tu nota del examen: "))
P = float(input("Ingresa tu nota de la presentacion: "))

PT = (T*0.3)
PI = (I*0.3)
NE = (E*0.3)
PP = (P*0.1)
N = (PT+PI+NE+PP)
N2 = round(N,1)
print("Tu nota final es: ",N2)