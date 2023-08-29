#Aprobación de créditos
ingreso= int(input("Ingrese Monto de ingreso: "))
año_de_nacimiento= int(input("ingrese año de nacimiento: "))
numero_de_hijos= int(input("Ingrese numero de hijos: "))
año_antiguedad= int(input("ingrese año de permanencia en el banco: "))
estado_civil= str(input("Ingrese estado civil (C:casado/S:soltero): "))
lugar_donde_vive= str(input("ingrese lugar donde vive (u:urbano/r:rural): "))
edad=2020-año_de_nacimiento

if (10 < año_antiguedad and 2 <= numero_de_hijos) or (estado_civil=="C" and 3 < numero_de_hijos and 45<= edad <=55) or \
        (ingreso>=2500000 and estado_civil=="S" and lugar_donde_vive=="U") or (ingreso>=3500000 and año_antiguedad>5)\
         or (lugar_donde_vive == "R" and estado_civil == "C" and numero_de_hijos<2):

    print("APROBADO")

else:
    print("RECHAZADO")
