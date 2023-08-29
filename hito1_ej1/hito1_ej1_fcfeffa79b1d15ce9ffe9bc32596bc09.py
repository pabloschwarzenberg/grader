#Nota final
PT= float(input("Ingrese Nota PT: "))
PI= float(input("Ingrese Nota PI: "))
NE= float(input("Ingrese Nota NE: "))
PP= float(input("Ingrese Nota PP: "))

NF=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print(round(NF,1))