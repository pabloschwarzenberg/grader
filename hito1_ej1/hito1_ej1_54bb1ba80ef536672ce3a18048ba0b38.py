#Nota final
PT = float(eval(input("Ingrese nota de su tarea : ")))
PI = float(eval(input("Ingrese nota de su interrogacion : ")))
NE = float(eval(input("Ingrese nota de su examen : ")))
PP = float(eval(input("Ingrese nota de su presentacion : ")))

nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP 

print("Su nota final es : ",nota_final)  