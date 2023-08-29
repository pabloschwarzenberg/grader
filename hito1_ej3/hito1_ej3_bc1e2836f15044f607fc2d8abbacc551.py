#Aprobación de créditos
income=int(input("Ingreso:"))
yborn=int(input("Año de nacimiento:"))
nchildren=int(input("Número de hijos:"))
y_in_bank=int(input("Años de pertenencia al banco:"))
civils=input("Estado civil:")
place=input("Si vive en campo o cuidad:")
if y_in_bank>10 and nchildren>=2:
    print("APROBADO")
else:
    if civils=="C" and nchildren>3 and (2016-yborn)>45 and (2016-yborn)<55:
        print("APROBADO")
    else:
        if income>2500000 and civils=="S" and place=="U":
            print("APROBADO")
        else:
            if income>3500000 and y_in_bank>5:
                print("APROBADO")
            else:
                if place=="R" and civils=="C" and nchildren<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")  