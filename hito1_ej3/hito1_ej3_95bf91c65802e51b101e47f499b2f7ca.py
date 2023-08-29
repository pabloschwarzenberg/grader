#Aprobación de créditos
Ingreso=int(input("Ingreso:"))
nacimiento=int(input("Año de nacimiento:"))
hijos=int(input("Número de hijos:"))
banco=int(input("Años de pertenencia al banco:"))
est=str(input("Estado civil:"))
vive=str(input("Si vive en campo o cuidad ("U": urbano, "R": rural):"))  
edad = 2017-nacimiento

if banco>10 and hijos>=2:
    print("APROBADO")

elif est =="C" and hijos>3 and (edad>45 and edad<55):
    print("APROBADO")
    
elif Ingreso>2500000 and est =="S" and vive=="U":
    print("APROBADO")

elif Ingreso>3500000 and banco>5:
    print("APROBADO")

elif vive=="R" and est =="C" and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO ")


