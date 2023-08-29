#Nota final
PT=float(input("dime tu nota de las tareas="))
PI=float(input("dime tu nota de las interrogaciones="))
NE=float(input("dime tu nota del examen="))
PP=float(input("dime tu nota de la presentacion="))
nota_final=round((0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP),1)
print("su nota final es",nota_final)