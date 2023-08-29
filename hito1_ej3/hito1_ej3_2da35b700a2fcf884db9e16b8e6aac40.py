#Aprobación de créditos


ingreso = int(input("Favor ingresar Ingresos (en pesos) sin $ ni puntuacion (Ej:100000) : "))
nacimiento = int(input("Favor ingresar año nacimiento(Ej:2001): "))
numeroHijos = int(input("Favor ingresar numero de hijos: "))
permanencia = int(input("Favor ingresar años de pertenencia al banco: "))
estadoCivil = input("Favor ingrese Estado Civil (S) Soltero, (C) Casado: ").upper()
campoCiudad = input("Favor ingrese (U) Urbano, (R) Rural: ").upper()
edad = 2021 - nacimiento

if permanencia > 10 and numeroHijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and numeroHijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso >= 2500000 and estadoCivil == "S" and campoCiudad == "U":
    print("APROBADO")
elif ingreso >= 3500000 and permanencia > 5:
    print("APROBADO")
elif campoCiudad == "R" and estadoCivil == "C" and numeroHijos < 2:
    print("APROBADO")
else:
    print("NO APROBADO")
