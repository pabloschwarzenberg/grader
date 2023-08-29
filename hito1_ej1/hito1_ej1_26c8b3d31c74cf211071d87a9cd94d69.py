#Nota final
PT=float(input("ingrese notas de PT:"))
NE=float(input("ingrese notas del NE:"))
PI=float(input("ingrese notas de PI:"))
PP=float(input("ingrese nota de PP:"))
nota_final=round((0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP),1)
print("su nota final es: ",nota_final)


