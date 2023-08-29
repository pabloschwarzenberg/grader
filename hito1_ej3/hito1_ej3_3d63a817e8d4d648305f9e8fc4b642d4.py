#Aprobación de créditos
ingreso = int(input("Ingrese su salario en pesos: $"))
año_nac = int(input("Ingrese su año de nacimiento: "))
n_hijos = int(input("¿Cuantos hijos tiene?: "))
años_pert = int(input("Ingrese los años de pertencia en el banco: "))
est_civil = str(input("Ingrese su estado civil. S=Soltero o C=Casado: "))
vive = str(input("¿Usted vive en campo o ciudad? U=ciudad o R=Campo: "))

if años_pert > 10 and n_hijos >= 2:
    print("APROBADO")
elif est_civil == "C" and n_hijos >3 and int(2021) - año_nac:
    print("APROBADO")
elif ingreso > 2500000 and est_civil == "S" and vive == "U":
    print("APROBADO")
elif ingreso > 3500000 and años_pert > 5:
    print("APROBADO")
elif vive == "R" and est_civil == "C" and n_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
