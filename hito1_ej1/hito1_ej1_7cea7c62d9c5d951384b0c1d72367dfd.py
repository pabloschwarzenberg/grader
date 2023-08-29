#Nota final
print("Ingrese sus notas ")
PT = float(input("Ingrese notas: "))
PI = float(input("Ingrese notas: "))
NE = float(input("Ingrese notas: "))
PP = float(input("Ingrese notas: "))
NP = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)
print("la nota de presentacion es : ","{:.1f}".format(NP))