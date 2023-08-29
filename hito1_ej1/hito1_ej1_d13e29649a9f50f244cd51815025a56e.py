PT=float(input(" "))
PI=float(input("Ingrese nota de interrogaciones: "))
NE=float(input("Ingrese nota del examen: "))
PP=float(input("Ingrese nota presentacion: "))

resultado= (0.3*PT) +(0.3*PI) + (0.3*NE)+(0.1*PP)
round(resultado,1)
print("su nota es: "+str(round(resultado,1)))