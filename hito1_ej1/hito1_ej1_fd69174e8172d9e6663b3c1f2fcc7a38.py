#Nota final
print("cálculo nota de presentación de exámen")

PT=float(input("inserte la nota de Tareas:"))
PI=float(input("inserte la nota de Interrogaciones:"))
NE=float(input("inserte la nota de Exámen:"))
PP=float(input("\ninserte la nota de Presentación:"))      
NF= 0.3*PT + 0.3*PI + 0.3*NE * 0.1*PP
print("El promedio final es de:"round(PP,1))