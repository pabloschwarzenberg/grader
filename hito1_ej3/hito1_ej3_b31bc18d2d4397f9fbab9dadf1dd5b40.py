#Aprobación de créditos
ingreso = int(input("Digite su ingreso sin puntos ni comas: "))
edad = int(input("Ingrese su año de nacimiento: " ))
hijos = int(input("Ingrese el numero de hijos que posee: "))
añosdelbanco = int(input("Ingrese la cantidad de años que ha sido cliente al banco: "))
sc = str(input("Ingrese su estado civil; si esta casado use una C mayuscula, de n\ lo contrario, si esta soltero use una S mayuscula: "))
lugar_geografico = str(input("Ingrese si su residencia se ubica en una zona urbana o rural con la respectiva inicial n\ de cada una en mayusculas (U o R): "))

nH = 2021-edad

if (añosdelbanco>10) and (hijos>=2):
    print ("APROBADO")
else:
    if ((nH >= 45) and (nH <=55)):
        print ("APROBADO")

    else: 
        if ( ingreso > 2500000) and (ec == "S") and (lugar_geografico == "U"):
            print ("APROBADO")

        else:
            if ( ingreso > 3500000 ) and (añosdelbanco > 5):
                print ("APROBADO")

            else:
                if (lugar_geografico == "R") and (ec == "C") and (hijos <2):
                    print ("APROBADO")

                else:
                    print("RECHAZADO")     