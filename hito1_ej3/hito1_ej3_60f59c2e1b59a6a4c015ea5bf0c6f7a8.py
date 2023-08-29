#Aprobación de créditos
Ingreso = int(input("Digite su ingreso en pesos: "))
AñodeNacimiento = int(input("Ingrese año de nacimiento: "))
númeroHijos = int(input("Ingrese cantidad de hijos: "))
AñosPertenenciaBanco = int(input("Ingrese sus años de pertenencia en el Banco: "))
estadoCivil = input("Ingrese S = Soltero o C = Casado: ")
Vivienda = input("Ingrese U = urbano o  R = rural: ")
Edad = 2020 - AñodeNacimiento
if (AñosPertenenciaBanco > 10) and (númeroHijos >= 2):
    print("APROBADO")

elif(estadoCivil == "C") and (númeroHijos > 3) and (Edad >= 45 and Edad <= 55):
    print("APROBADO")

elif(Ingreso > 2500000) and (estadoCivil == "S") and (Vivienda == "U"):
    print("APROBADO")

elif(Ingreso > 3500000) and (AñosPertenenciaBanco > 5):
    print("APROBADO")

elif(Vivienda == "R") and (estadoCivil == "C") and (númeroHijos < 2):
    print("APROBADO")

else:
    print("RECHAZADO")