#Nota final
T = float(input("Favor ingrese nota obtenida en las tareas:"))
I = float(input("Favor ingrese nota obtenida en las interrogaciones:"))
E = float(input("Favor ingrese nota obtenida en el examen:"))
P = float(input("Favor ingrese nota obtenida enn la presentacion:"))

PT = (T*0.3)
PI = (I*0.3)
NE = (E*0.3)
PP = (P*0.1)

N = (PT+PI+NE+PP)
N2 = round(N,1)

print("La nota final es:",N2)      