#Aprobación de créditos
salario = int(input("Ingrese su salario $: "))
nac = int(input("Ingrese su año de nacimineto: "))
hijos = int(input("Ingrese cantidad de hijos: "))
pert_b = int(input("Ingrese hace cuantos años pertenece al banco: "))
edo_civil = str(input("Ingrese su edo. civíl; ""S"": soltero, ""C"", casado: "))
zona = str(input("Ingrese donde vive, si es ciudad marque ""U"", si es campo marque ""R"": "))

if pert_b >= 10 and hijos >= 2:
    print("APROBADO")

elif edo_civil == "C" and hijos > 3 and nac in range [1967 or 1977]:
    print("APROBADO")

elif salario > 2500000 and edo_civil == "S" and zona == "U":
    print("APROBADO")

elif salario > 3500000 and pert_b > 5:
    print("APROBADO")

elif zona == "R" and edo_civil == "C" and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")

