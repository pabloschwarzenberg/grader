#Aprobación de créditos
print("ingrese datos")
ing = float(input("ingreso="))
ano = int(input("año de nacimiento="))
hijos = int(input("numeros de hijos="))
tiempo = float(input("tiempo en su banco="))
civil = input("Estado civil (S: soltero, C: casado)=")
vive = input("Si vive en campo o cuidad (U: urbano, R: rural)=")
edad = 2021 - ano
if((civil=="S"or civil=="C")and(vive=="U"or vive=="R")): 
    if(ano > 10) and (hijos >= 2):
        print("APROBADO")
    elif((civil)=="C") and (hijos > 3) and (edad >= 45) and (edad <= 55):
        print("APROBADO")
    elif((ing > 2500000) and ((civil)=="S") and (vive)=="U"):
        print("APROBADO")
    elif((ing > 3500000) and (tiempo > 5)):
        print("APROBADO")
    elif(((vive)=="R") and ((civil)=="C") and (hijos < 2)):
         print("APROBADO")
    else:
        print("RECHAZADO")
else:
    print("INGRESE BIEN LOS DATOS")
      