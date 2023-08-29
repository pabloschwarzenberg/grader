#Aprobación de créditos
#from datetime import datetime
#ahora = datetime.now()
#print("Justo ahora es:", ahora)


ingreso = float(input("Digite ingreso mensual:"))
fechaNac = int(input("Digite año de nacimiento Ej: '1985':"))
Nhijos = int(input("Digite cantidad de hijos:"))
aniosbanco = int(input("Digite años de pertenencia en el banco:"))
estadocivil = str(input("Digite estado civil Ej: 'S' si es soltero, 'C' si es casado:"))
camOciu = str(input("Digite si vive en campo o ciudad Ej: 'U' si es urbano, 'R' si es rural "))

cam =  camOciu.upper()
estado = estadocivil.upper()

anio = 2021

aniosUser = anio - fechaNac

#print("Visualizar: ", estado )





if aniosUser > 45 and aniosUser <=55 and Nhijos >= 3 and estado == "C" and ingreso >= 2500000 and cam == "U":
    print("APROBADO ")


elif aniosbanco > 5 and ingreso >= 3500000:
    print("APROBADO ")

elif aniosbanco > 10 and Nhijos >= 2:

    print("APROBADO ")


elif cam == "R" and estado == "C" and Nhijos <= 2:

    print("APROBADO ")

else:
    print("RECHAZADO  ")

