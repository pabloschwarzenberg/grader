#Aprobación de créditos
ingreso = float(input("ingrese su sueldo en pesos: "))
año = int(input("ingrese año de nacimiento: "))
num_hijo = int(input("ingrese cuantos hijos tiene: "))
ant = int(input("cuantos años lleva como cliente en el banco: "))
est_civil = str(input("estado civil (S) para soltero o (C) para casado: "))
direccion = str(input("ingrese (U) si vive en ciudad o (R) si vive en el campo: "))
edad = 2020 - año
if ant >= 10 and num_hijo >= 2:
    print("APROBADO")
else:
    if est_civil == str("C") and num_hijo >= 3 and  edad >=45 and edad <=55:
            print("APROBADO")
    else:
        if ingreso >= 2500000 and est_civil == str("S") and direccion == str("U"):
            print("APROBADO")
        else:
            if ingreso >= 3500000  and ant >= 5:
                print("APROBADO")
            else:
                if direccion == str("R") and est_civil == str("C") and num_hijo <= 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")