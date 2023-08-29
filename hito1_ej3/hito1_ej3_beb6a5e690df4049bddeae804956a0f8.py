#Aprobación de créditos
def aprobar_el_credito_del_banco(ingresos, nacimiento, hijos, años_en_el_banco, estadocivil, ubicacion):
#definir las variables que se utilizaran    
    if años_en_el_banco > 10 and hijos >= 2:
        print("APROBADO")
    elif estadocivil == "C" and hijos > 3 and 1980 <= nacimiento <= 1970:
        print("APROBADO")
    elif ingreso > 2500000 and estadocivil == "S" and ubicacion == "U":
        print("APROBADO")
    elif ingreso > 3500000 and años_en_el_banco > 5:
        print("APROBADO")
    elif ubicacion == "R" and estadocivil == "C" and hijos < 2:
        print("APROBADO")
    else:
        print("Rechazado")
#colocar los condicionantes necesarios para el credito del banco, con if, elif, else

ingreso = int(input("Coloque su ingreso (en pesos): "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
años_en_el_banco = int(input("Ingrese los años de pertenencia al banco: "))
estadocivil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano(ciudad), R para rural(campo)): ")
#preguntar los valores para ver si es apto para el credito
res = aprobar_el_credito_del_banco(ingreso, nacimiento, hijos, años_en_el_banco, estadocivil, ubicacion)