#Aprobación de créditos
def aprobar_credito(ingreso,año_nacimiento,num_hijos,años_pertenencia,estado_civil,lugar_residencia):
    if años_pertenencia>10 and num_hijos>=2:
        return True
    if estado_civil=="C" and num_hijos<3 and 45<=(2023-año_nacimiento)<=55:
        return True 
    if ingreso>2500000 and estado_civil=="S" and lugar_residencia=="U":
        return True 
    if ingreso>3500000 and años_pertenencia>5:
         return True
    if lugar_residencia=="R" and estado_civil=="C" and num_hijos<2:
        return True
    return False

ingreso=int(input("Ingreso mensual: "))
año_nacimiento=int(input("Año de nacimiento: "))
num_hijos=int(input("Numero de hijos: "))
años_pertenencia=int(input("Años de pertenencia al banco: "))
estado_civil=input("Estado civil (S:soltero,C:casado): ")
lugar_residencia=input("Lugar de residencia (U:urbano,R:rural): ")
if aprobar_credito(ingreso,año_nacimiento,num_hijos,años_pertenencia,estado_civil,lugar_residencia):
    print("APROBADO")
else:
    print("RECHAZADO")      