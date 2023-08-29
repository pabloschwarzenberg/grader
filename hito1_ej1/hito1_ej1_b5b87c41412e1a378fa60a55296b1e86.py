#Nota final
PT=float(input("Escriba la nota: "))
PI=float(input("Nota de las interrogaciones: "))
NE=float(input("Nota de examen: "))
PP=float(input("Nota de presentacion: "))

nota_final=PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1
round(nota_final)
print("Su nota final es:",nota_final)