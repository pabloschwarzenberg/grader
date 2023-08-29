#Aprobación de créditos
i = int(input("Ingreso: "))
año_n = int(input("Año de nacimiento: "))
nh = int(input("Número de hijos: "))
a_p_b = int(input("Años de pertenencia al banco: "))
ec = str(input("Estado civil (""S"": soltero, ""C"", casado): "))
cc = str(input("Si vive en campo o cuidad ("U": urbano, "R": rural): "))



if a_p_b >= 10 and nh >= 2:
    a = 1
elif ec == "C" and nh > 3 and (año_n >= 45 and año_n <= 55):
    a = 1
elif i >= 2500000 and ec == "S" and cc == "U":
    a = 1
elif i >= 3500000 and a_p_b > 5:
    a = 1
elif cc == "R" and ec == "C" and nh <= 2:
    a = 1
if a == 1:
    print("APROBADO")
else:
    print("RECHAZADO")