#Aprobación de créditos
#Entrada
year_actual = 2022

Ingreso = float(input("Ingresos(en pesos): "))

year = int(input("Ingrese año de nacimiento: "))

edad = year_actual - year

hijos = int(input("Ingrese numero de hijos: "))

pertenencia = int(input("Ingrese años de pertenencia al banco: "))

e_Civil = str(input("(S)oltero o (C)asado: ")).upper()

vive = str(input("¿Vive en campo o ciudad? 'U' campo 'R' rural: ")).upper()

#Procedimiento
if pertenencia >= 10 and hijos >= 2:
    print("APROBADO")
else:
    if (e_Civil == "C" and hijos >= 3) and (edad >= 45 and edad <= 55):
        print("APROBADO")
    else:
        if Ingreso > 2500000 and e_Civil == "S" and vive == "U":
            print("APROBADO")
        else:
            if Ingreso > 3500000 and pertenencia > 5:
                print("APROBADO")
            else:
                if vive == "R" and e_Civil == "C" and hijos < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
