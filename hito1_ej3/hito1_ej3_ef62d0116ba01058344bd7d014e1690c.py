#Ingresar datos
ingreso=int(input("Ingrese Ingreso: "))
año_nacimiento= int(input("Ingrese el año de nacimiento: "))
hijos=int(input("Ingrese la cantidad de hijos que tenga: "))
años_banco=int(input("Ingrese la cantidad de años que pertenece al banco: "))
estado_civil=input("Ingrese estado civil, S (Soltero) o C (Casado) : ")
lugar=input("Ingrese la letra si vive en campo U (urbano) o R (Rural): ")

#Reglas y Desarrollo
edad= 2020 - año_nacimiento

if años_banco > 10 and hijos <= 2:
    print("APROBADO")
elif estado_civil == str('C') or str('c') and hijos >= 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == str('C') or estado_civil == str('c')  and lugar == str('U') or lugar == str('u'):
    print("APROBADO")
elif ingreso > 3500000 and años_banco >= 5:
    print("APROBADO")
elif lugar == str('R') or lugar == str('r') and estado_civil == str('C') or estado_civil == str('c')  and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZO")
