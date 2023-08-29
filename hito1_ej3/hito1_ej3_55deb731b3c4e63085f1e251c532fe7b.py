#Aprobación de créditos
I = int(input("Ingrese su Ingreso en pesos: "))
AN = int(input("Ingrese su año de nacimineto: "))
NH = int(input("Ingrese su número de hijos: "))
APB = int(input("Ingrese los años que ha pertenecido al banco: "))
EC = input("Ingrese su estado civil: \n S. es soltero \n C. es casado ")
V = input("Ingrese en dónde vive: \n U. Urbano \n R. Rural ")
ANF = 2020 - AN
if APB > 10 and NH > 1:
    print("APROBADO")
elif EC == "C" and 56 > ANF < 44:
    print("APROBADO")
elif I > 3500000 and APB > 5:
    print("APROBADO")
elif V == "R" and NH < 2:
    print("APROBADO")
else:
    print("RECHAZADO")