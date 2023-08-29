#Aprobación de créditos
Ingreso = int(input("Ingresos en pesos: "))
Ano = int(input("Ano de nacimiento: "))
Hijos = int(input("Numero de hijos: "))
AnosBanco = int(input("Anos de pertenencia al banco: "))
Ecivil = str(input("Soltero (S) o Casado (C): "))
UoR = str(input("Vive en zona Urbana (U) o Rural (R): "))

C = Ecivil
S = Ecivil
U = UoR
R = UoR
Edad = 2021 - Ano

if (AnosBanco > 10 and Hijos >= 2):
    print("CREDITO APROBADO")
elif (Ecivil[0] == C and Hijos > 3 and Edad > 45 and Edad < 55):
    print("CREDITO APROBADO")
elif (Ingreso > 2500000 and Ecivil[0] == S and UoR[0] == U):
    print("CREDITO APROBADO")
elif (Ingreso > 3500000 and AnosBanco > 5):
    print("CREDITO APROBADO")
elif (UoR[0] == R and Ecivil[0] == C and Hijos < 2):
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")
      