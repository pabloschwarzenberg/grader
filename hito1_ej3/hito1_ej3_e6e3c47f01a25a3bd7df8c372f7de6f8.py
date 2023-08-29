#Aprobación de créditos
import datetime
print("Sistema Automatizado de aprobación de créditos\n\n****Datos postulante****")
ingreso=int(input("Ingreso: $"))
a_nacimiento=int(input("Año de nacimiento: "))
num_hijos=int(input("Número de hijos: "))
a_pert_banco=int(input("Años de pertenencia al banco: "))
estado_civil=input("Estado civil (S:Soltero / C: Casado): ")
lugar_vive=input("Lugar donde vive (U: urbano / R:rural): ")

date = datetime.date.today()
a_actual = int(date.strftime("%Y"))
edad = a_actual - a_nacimiento

if a_pert_banco > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil=="C" and num_hijos>3 and edad >=45 and edad<=55:
    print("APROBADO")
elif ingreso>3500000 and a_pert_banco >5:
    print("APROBADO")
elif lugar_vive == "R" and estado_civil=="C" and num_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")   