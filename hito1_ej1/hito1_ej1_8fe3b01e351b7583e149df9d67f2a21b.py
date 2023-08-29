#Nota final
Pt = float(input("nota de las tareas:"))      
Pi = float(input("nota de las interrogaciones:"))     
Ne = float(input("nota del examen:"))     
Pp = float(input("nota de presentacion:"))     
X = (0.3*Pt) + (0.3*Pi) + (0.3*Ne) + (0.1*Pp)
print("el promedio final es: %5.1f" %(X))