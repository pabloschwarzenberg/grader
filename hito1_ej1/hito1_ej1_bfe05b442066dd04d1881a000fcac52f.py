#Nota final
 #Benyi
PT=float(input("La nota de tu tarea "))
PI=float(input("La nota de tu interrogacion "))
NE=float(input("La nota de tu examen "))
PP=float(input("La nota de tu presentacion "))
NF=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Tu nota final es", round(NF,1))     