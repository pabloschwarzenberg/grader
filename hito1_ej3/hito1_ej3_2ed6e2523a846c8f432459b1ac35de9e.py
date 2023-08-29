#Aprobación de créditos
import datetime
ingreso = int(input("Favor ingrese su ingreso mensual :"))
year = int(input("Ingrese Año de Nacimiento :"))
anactual = datetime.datetime.now().year
while not (year >= 1900 and year <=anactual):
    year = int(input("Error : Ingrese Año de Nacimiento :"))
hijos = int(input("Cantidad de Hijos :"))
antigue = int(input("Años de pertenencia al banco :"))
ecivil = input("Ingrese estado Civil (S = Soltero o C = Casado):")
while not(ecivil=="S" or ecivil=="C"):
    ecivil = int(input("Error : Ingrese estado Civil (S = Soltero o C = Casado):"))
vive = input("Indique donde vive (U = urbano o R = rural):")
while not(vive=="U" or vive=="R"):
    vive = int(input("Error : Indique donde vive (U = urbano o R = rural):"))
edad = anactual - year
if (antigue > 10 and hijos >= 2):
    print ("APROBADO")
elif (ecivil == "C" and hijos >=3 and edad >= 45 and edad <=55):
    print ("APROBADO")
elif (ingreso >= 2500000 and ecivil =="S" and vive == "U"):
    print ("APROBADO")
elif (ingreso >= 3500000 and antigue >=5):
    print ("APROBADO")
elif (vive == "R" and ecivil =="C" and hijos <= 2):
    print ("APROBADO")
else:
    print ("RECHAZADO")