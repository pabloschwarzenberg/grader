D=int(input("ingrese sus ingresos :"))
Na=int(input("Ingrese su año de nacimiento :"))
NH=int(input("Ingrese numero de hijos :"))
BA=int(input("Ingrese la cantidad de años de afiliacion en el banco"))
Ec=str(input("Estado civil :"))
Lr=str(input("Lugar de residencia (Urbano,Rural)"))

if (BA >= 10) and (NH >= 2):
    print("APROBADO")
elif (Ec =="C") and (NH > 3) and (Na >=44 or 55):
    print("APROBADO")
elif(D>25000000) and (Ec== "S") and (Lr=="U"):
    print("APROBADO")
elif (D > 3500000) and (BA == 5):
    print("APROBADO")
elif (Lr=="R") and (Ec=="C") and (NH<2):
   print("APROBADO")
else:
    print("Credito rechasado")