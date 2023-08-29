#Aprobación de créditos
Ingreso = int(input("Digite su ingreso en pesos: "))
AnodeNacimiento = int(input("Ingrese año de nacimiento: "))
numeroHijos = int(input("Ingrese cantidad de hijos: "))
AnosPertenenciaBanco = int(input("Ingrese sus años de pertenencia en el Banco: "))
estadoCivil = input("Ingrese S = Soltero o C = Casado: ")
Vivienda = input("Ingrese U = urbano o  R = rural: ")
Edad = 2020 - AnodeNacimiento
if (AnosPertenenciaBanco > 10) and (numeroHijos >= 2):
    print("APROBADO")
elif (estadoCivil == "C") and (numeroHijos > 3) and (Edad >= 45 and Edad <= 55):
    print("APROBADO")
elif (Ingreso > 2500000) and (estadoCivil == "S") and (Vivienda == "U"):
    print("APROBADO")
elif (Ingreso > 3500000) and (AnosPertenenciaBanco > 5):
    print("APROBADO")
elif (Vivienda == "R") and (estadoCivil == "C") and (numeroHijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
      