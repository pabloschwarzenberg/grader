#Aprobación de créditos
ingreso=int(input("Ingrese su valor de ingreso en pesos: "))
nacimiento=int(input("Ingrese el año de nacimiento: "))
hijos=int(input("Ingrese su número de hijos: "))
pertenencia=int(input("Ingrese su año de pertenencia al banco: "))
civil=input("Ingrese su estado civil (S: soltero - C: casado): ")
recidencia=input("Ingrese si vive en campo o en ciudad (U: urbano - R: rural): ")

edad= 2021-nacimiento

if(pertenencia>10 and hijos>=2):
    print("APROBADO")
else: 
    if(civil =="C" and hijos>3 and (edad>=45 and edad<=55)):
        print("APROBADO")
    else:
        if(ingreso>=2500000 and civil=="S" and recidencia=="U"):
            print("APROBADO")
        else: 
            if(ingreso>=3000000 and pertenencia>5):
                print("APROBADO")
            else:
                if(recidencia=="R" and civil=="C" and hijos<2):
                    print("APROBADO")
                else:
                    print("RECHAZADO")