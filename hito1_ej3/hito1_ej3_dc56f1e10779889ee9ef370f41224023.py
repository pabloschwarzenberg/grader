#Aprobación de créditos
ing = eval(input("ingreso: $"))
ano = eval(input("año de naciminto: "))
numh = eval(input("Número de hijos: "))
añob = eval(input("Años de pertenencia al banco: "))
estc = input("Estado civil (""S"": soltero, ""C"", casado): ")
UR = input("Si vive en campo o cuidad (""U"": urbano, ""R"": rural):")

x = 2020-ano

if añob > 10 and numh >= 2:
    print("APROBADO")

elif estc == "C" and numh > 3 and 45 > x >55:
    print("APROBADO")

elif ing > 250000 and estc == "S" and UR == "U":
    print("APROBADO")

elif UR == "R" and estc == "C" and numh < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
