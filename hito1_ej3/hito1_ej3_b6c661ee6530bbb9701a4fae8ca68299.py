#Aprobación de créditos
ingreso = int(input("Monto de sus ingresos mensuales: "))
añoNacimiento = int(input("Du año de nacimiento es:  "))
numeroHijos = int(input("Numero de hijos: "))
añosEnBanco = int(input("Años de pertencia en el banco: "))
estadoCivil = input("Su estado civil es: S: soltero, o C: casado: ")
viveEn =  input("Vive en campo (R) o Ciuddad (U): ")

edad = 2020 - añoNacimiento

condicion1 = (añosEnBanco >= 10) and (numeroHijos >= 2)
condicion2 = (estadoCivil.upper() == "C") and (numeroHijos > 3) and (55 >= edad >= 45)
condicion3 = (ingreso >= 2500000) and (estadoCivil.upper() == "S") and (viveEn.upper() == "U")
condicion4 = (ingreso >= 3500000) and (añosEnBanco > 5)
condicion5 = (viveEn.upper() == "R") and (estadoCivil.upper() == "C") and (numeroHijos < 2)

if (condicion1 == True) or (condicion2 == True) or (condicion3 == True) or (condicion4 == True) or (condicion5 == True):
    print("APROBADO")
else:
    print("RECHAZADO")