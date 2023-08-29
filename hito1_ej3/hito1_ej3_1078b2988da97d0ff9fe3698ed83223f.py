#Aprobación de créditos


ingreso = int(input("Ingreso (en pesos): "))
ano = int(input("Ingrese año de nacimiento: "))
Ndehijos = int(input("Ingrese numero de hijos: "))
anosPertenencia = int(input("Ingrese años de pertenencia al banco: "))
estadocivil = input("Estado civil (S: Soltero, C: Casado): ")
vivienda = input("Vivienda (U: Urbano, R: rural): ")

anos = 2023 - ano

if anosPertenencia > 10 and Ndehijos > 1:
    print("Aprobado")
elif estadocivil == "C" and Ndehijos > 3 and 45 <= anos <= 55:
    print("Aprobado")
elif ingreso >= 250000 and estadocivil == "S" and vivienda == "U":
    print("Aprobado")
elif ingreso >= 350000 and anosPertenencia > 5:
    print("Aprobado")
elif vivienda == "R" and estadocivil == "C" and Ndehijos < 3:
    print("Aprobado")
else:
    print("Rechazado")
