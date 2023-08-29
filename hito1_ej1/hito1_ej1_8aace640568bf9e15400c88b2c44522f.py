#Nota final
PT = float(input("Ingrese nota de las tares"))
PI = float(input("Ingrese nota de las interrogaciones"))
NE = float(input("Ingrese nota del examen"))
PP = float(input("Ingrese nota de presentación"))
promedio = PT*0.3 + PI*0.3 + NE*.3 + PP*0.1
print("Su promedio final es de:","{:.1f}".format(promedio))