#Nota final
def promedio(n1,n2,n3,n4):
    programa=0.3*n1+0.3*n2+0.3*n3+0.1*n4
    promedio=round(programa,1)
    return promedio
NT=float(input("Ingrese nota tareas:"))
NI=float(input("Ingrese nota intterrogaciones:"))
NE=float(input("Ingrese nota de examen:"))
NP=float(input("Ingrese nota de presentación:"))
print(promedio(NT,NI,NE,NP))