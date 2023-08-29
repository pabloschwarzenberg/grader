ingreso = eval(input("Ingreso (en pesos): "))
nacimiento = int(input("Año de nacimiento: "))
edad = (2021 - nacimiento)
hijos = int(input("Número de hijos: ")) 
antiguedad = int(input("Años de pertenencia al banco: "))
estado_civil = str(input("Estado civil (S: soltero, C, casado): "))
estado_civil_lower = estado_civil.lower()
zona = str(input("Si vive en campo o cuidad (U: urbano, R: rural): "))

if antiguedad >= 10 and hijos >= 2:
    print("APROBADO")
else:
    if estado_civil_lower == "C" and hijos >= 3 and edad >= 45 or edad <= 55:
        print("APROBADO")
    else:
        if ingreso > 2500000 and estado_civil_lower == "S" and zona == "U":
            print("APROBADO")
        else:
            if ingreso > 3500000 and antiguedad >= 5:
                print("APROBADO")
            else:
                if zona == "R" and estado_civil_lower == "C" and hijos < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
"""
# Pedir datos

ingreso = eval(input("Ingreso en CLP: "))
año_nacimiento = eval(input("Ingrese año de nacimiento: "))
numero_hijos = eval(input("Ingrese la cantidad de hijos que tiene: "))
años_usuario_banco = eval(input("Ingrese cuantos años lleva como usuario: "))
estado_civil = input("Estado civil (S: Soltero, C: Casado) " )
zona = input("¿Vive en zona urbana o rural (U: Urbano, R: Rural)? ")

# Hoja de calculo

edad = 2020 - año_nacimiento

# Desarollo

if años_usuario_banco > 10 and numero_hijos >= 2:
    print("APROBADO")
else:
    if estado_civil == "C" or "c" and numero_hijos > 3 and año_nacimiento [45,55]:
        print("APROBADO")
    else:
        if ingreso > 2500000 and estado_civil == "S" or "s" and zona == "U" or "u":
            print("APROBADO")
        else:
            if ingreso > 3500000 and años_usuario_banco > 5:
                print("APROBADO")
            else:
                if zona == "R" or "r" and estado_civil == "C" or "c" and numero_hijos < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO)
"""
