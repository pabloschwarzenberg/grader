#Aprobación de créditos
Ingreso = int(input("Ingrese los ingresos que gana en pesos: "))
AñoNacimiento = int(input("Ingrese su año de nacimiento: "))
NumeroHijos = int(input("Ingrese su numero de hijos: "))
AñosEnBanco = int(input("Ingrese la cantidad de años que lleva de cliente en el banco: "))
Estadocivil = input("Ingrese su estado civil, S para soltero y C para casado: ")
CampoOCiudad = input("Ingrese si vive en el campo o ciudad, U para urbano y R para rural: ")
if AñosEnBanco > 10 and NumeroHijos >= 2:
    print("APROBADO")
elif Estadocivil == 'C' and NumeroHijos > 3 and AñoNacimiento >= 1965 and AñoNacimiento <= 1975:
    print("APROBADO")
elif Ingreso > 2500000 and Estadocivil == 'S' and CampoOCiudad == 'R':
    print("APROBADO")
elif Ingreso > 3500000 and AñosEnBanco > 5:
    print("APROBADO")
elif CampoOCiudad == 'R' and Estadocivil == 'C' and NumeroHijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      