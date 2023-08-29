#Aprobación de créditos
ingreso=float(input("ingrese monto en pesos"))
ano_nacimiento=int(input("ingrese año de nacimiento:_"))
edad=2021-ano_nacimiento
numero_hijos=int(input("Ingrese numero de hijos:"))
anodeper=int(input("ingrese año los años de pertenencia al banco" ))
estado=input("ingrese estado civil (S: soltero   C:casado")
vivienda =input("ingrese donde vive (U:urbano R: rural")

if anodeper>10 and numero_hijos>=2:
    print("APROBADO")
else:
    if (estado== "c" or estado =="C") and numero_hijos >3 and (edad>45 and edad<55):
        print("APROBADO")
    else:
        if ingreso>3500000 and anodeper >5:
            print("APROBADO")
        else:
            if (vivienda =="R" or vivienda =="R") and (estado == "c" or estado == "C") and numero_hijos<2:
                print("APROBADO")

            else:
                print("DESAPROBADO") 