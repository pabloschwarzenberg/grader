#Aprobación de créditos
Ingreso = int(input("Ingrese su ingreso en pesos: "))
Anonacimiento = int(input("Ingrese su año de nacimiento: "))
Edad = 2022 - Anonacimiento
Numerohijos = int(input("Ingrese su número de hijos: "))
Anosbanco = int(input("Ingrese su ingreso en pesos: "))
Estadocivil = str(input("Ingrese su estado civil (S) Soltero o (C) Casado: "))
Vives = str(input("Ingrese donde vive (U) Urbano o (R) Rural: "))

if Anosbanco > 10 and Numerohijos >= 2:
    print("APROBADO")
elif Estadocivil == "C" and Numerohijos > 3 and 45 < Edad < 55:
    print("APROBADO")
elif Ingreso > 2500000 and Estadocivil == "S" and Vives == U:
    print("APROBADO")
elif Ingreso > 3500000 and Anosbanco > 5:
    print("APROBADO")
elif Vives == "R" and Estadocivil == "C" and Numerohijos < 2:
    print("APROBADO")
else:
    print("REPROBADO")

