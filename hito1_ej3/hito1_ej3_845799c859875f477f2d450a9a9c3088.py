Ingreso = int(input("Cuanto es tu ingreso?: "))
AN = int(input("Ingresa tu año de nacimiento: "))
NdH = int(input("Ingresa numero de hijos: "))
AB = int(input("Ingresa años de pertenencia al banco: "))
Ec = str(input("S: soltero - C: casado: "))
CoC = str(input("U: urbano - R: rural: "))

if AB > 10 and NdH >= 2:
    print("APROBADO")
elif Ec == "C" and NdH > 3 and (2022 - AN) >= 45 and (2022 - AN) <= 55:
    print("APROBADO")
elif Ingreso > 2500000 and Ec == "S" and CoC == "U":
    print("APROBADO")
elif Ingreso > 3500000 and AB > 5:
    print("APROBADO")
elif CoC == "R" and Ec == "C" and NdH < 2:
    print("APROBADO")
else:
    print("RECHAZADO")