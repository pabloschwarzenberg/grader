#Aprobación de créditos
ingresos = int(input("Ingresos : "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2020 - año_nacimiento
años_banco = int(input("años en el banco "))
numero_hijos = int(input("Número de hijos: "))
estado_civil = input("Estado civil c si es casado y s si es soltero" )
zona = input("vive en zona rural una r si vive en zona urbana una u ")

if años_banco > 10 and numero_hijos >= 2:
    print("APROBADO")
else:
    if estado_civil == "C" or "c" and numero_hijos > 3 and 45 <= edad <= 55:
        print("APROBADO")
    else:
        if ingresos > 2500000 and estado_civil == "S" or "s" and zona == "U" or "u":
            print("APROBADO")
        else:
            if ingresos > 3500000 and años_banco > 5:
                print("APROBADO")
            else:
                if zona == "R" and estado_civil == "C" or "c" and numero_hijos < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")      