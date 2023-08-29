#Aprobación de créditos
ingreso = int(input("Digite su ingreso sin puntos ni comas: "))
edad = int(input("Ingrese su año de nacimiento: " ))
hijos = int(input("Ingrese el numero de hijos que posee: "))
years = int(input("Ingrese la cantidad de años que ha sido cliente al banco: "))
sc = str(input("Ingrese su estado civil; si esta casado use una C mayuscula, de n\ lo contrario, si esta soltero use una S mayuscula: "))
campo_ciudad = str(input("Ingrese si su residencia se ubica en una zona urbana o rural con la respectiva inicial n\ de cada una en mayusculas (U o R): "))

n1 = 2021-edad

if (years>10) and (hijos>=2):
    print ("APROBADO")
else:
    if ((n1 >= 45) and (n1 <=55)):
        print ("APROBADO")

    else: 
        if ( ingreso > 2500000) and (sc == "S") and (campo_ciudad == "U"):
            print ("APROBADO")

        else:
            if ( ingreso > 3500000 ) and (years > 5):
                print ("APROBADO")

            else:
                if (campo_ciudad == "R") and (sc == "C") and (hijos <2):
                    print ("APROBADO")

                else:
                    print("RECHAZADO")

      