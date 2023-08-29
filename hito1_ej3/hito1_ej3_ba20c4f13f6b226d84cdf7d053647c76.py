#Aprobación de créditos
ing = float(input("Ingrese el ingreso en pesos: "))
nac = int(input("Ingrese el año de nacimiento: "))
num = int(input("Ingrese el número de hijos: "))
per = int(input("Ingrese los años de pertenencia al banco: "))
est = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubi = input("Ingrese la ubicación (U para urbano, R para rural): ")

if per > 10 and num >= 2:
    print("APROBADO")
elif est == "C" and num > 3 and 45 <= (2023 - nac) <= 55:
    print("APROBADO")
elif ing > 2500000 and est == "S" and ubi == "U":
    print("APROBADO")
elif ing > 3500000 and per > 5:
    print("APROBADO")
elif ubi == "R" and est == "C" and num < 2:
    print("APROBADO")
else:
    print("RECHAZADO")     