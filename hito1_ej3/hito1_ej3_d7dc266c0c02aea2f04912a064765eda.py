#Aprobación de créditos
ingreso = int(input("Ingrese la cantidad de ingreso: "))
añoNacimiento = int(input("Ingrese su año de nacimiento: "))
Nhijos = int(input("Ingrese el número de hijos: "))
añosPB = int(input("Ingrese años de pertenencia al banco: "))
estadoCivil = input("Ingrese su estado civil 'S' o 'C': ")
campoCiudad = input("Ingrese en donde vive 'U' o 'R': ")
estadoCivil.upper()
campoCiudad.upper()
añoNacimiento = 2020 - añoNacimiento

if añosPB > 10 and Nhijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and Nhijos > 3 and añoNacimiento >= 45 or añoNacimiento <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estadoCivil == "S" and campoCiudad == "U":
    print("APROBADO")
elif ingreso > 3500000 and añosPB > 5:
    print("APROBADO")
elif campoCiudad == "R" and estadoCivil == "C" and Nhijos < 2:
    Print("APROBADO")
else:
    print("RECHAZADO")  