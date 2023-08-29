#Aprobación de créditos
Ingreso = int(input("Ingrese su sueldo mensual (en pesos): $"))
Anonac = int(input("Ingrese su año de nacimiento (aaaa): "))
Hijos = int(input("Ingrese cantidad de hijos: "))
Anobanco = int(input("Ingrese años de antiguedad en nuestro banco: "))
EstCivil = str(input("Ingrese su estado civil (S: soltero o C : casado): "))
Vive = str(input("Ingrese si vive en campo o cuidad (U: urbano, R: rural): "))

C = 1
S = 0
U = 1
R = 0
Edad = 2020 - Anonac

if Anobanco > 10 and Hijos >= 2:
    print("Crédito APROBADO")
elif EstCivil == C and Hijos > 3 and Edad >= 45 and Edad <= 55:
    print("Crédito APROBADO")
elif Ingreso > 2500000 and EstCivil == S and Vive == U:
    print("Crédito APROBADO")
elif Ingreso > 3500000 and Anobanco > 5:
    print("Crédito APROBADO")
elif Vive == R and EstCivil == C and Hijos < 2:
    print("Crédito APROBADO")
else:
    print("No cumple con los requisitos")
    print("Crédito RECHAZADO")     