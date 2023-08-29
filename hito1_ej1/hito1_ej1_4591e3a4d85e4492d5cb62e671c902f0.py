#Nota final
print("CALCULO DE NOTA FINAL")
T=float(input("INGRESE LA NOTA DE LA TAREA: "))
I=float(input("INGRESE LA NOTA DE LA INTERROGACION: "))
E=float(input("INGRESE LA NOTA DEL EXAMEN: "))
P=float(input("INGRESE LA NOTA DE LA PRESENTACION: "))
X=(0.3*T)+(0.3*I)+(0.3*E)+(0.1*P)
Y= round(X,1)
print("LA NOTA FINAL ES DE: ", Y)      