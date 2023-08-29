#Nota final
PT=float(input("Ingrese su nota de tareas "))
while (PT<1 or PT>7):
    PT=float(input("Ingrese su nota de tareas "))
PI=float(input("Ingrese su nota de interrogaciones "))
while (PI<1 or PI>7):
    PI=float(input("Ingrese su nota de interrogaciones "))
NE=float(input("Ingrese su nota del examen "))
while (NE<1 or NE>7):
    NE=float(input("Ingrese su nota del examen "))
PP=float(input("Ingrese su nota de presentación "))
while (PP<1 or PP>7):
    PP=float(input("Ingrese su nota de presentación "))
PF=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El promedio final es",round(PF,1))