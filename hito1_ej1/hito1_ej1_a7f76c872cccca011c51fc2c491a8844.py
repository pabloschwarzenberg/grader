
PT= float(input("Ingrese nota PT: "))
PI= float(input("Ingrese nota PI: "))
NE= float(input("Ingrese nota NE: "))
PP= float(input("Ingrese nota PP: "))

#PROCESAMIENTO

Nota_Final= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

#SALIDA

print("Estimadx su nota final es", round(Nota_Final,1))