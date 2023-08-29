#Aprobación de créditos
ingreso = int(input("ingreso en pesos: "))
año_nacim = int(input("ingrese año de nacimiento: "))
num_hijos = int(input("ingrese numero hijos: "))
año_perten = int(input("ingrese año de pertenencia al banco: "))
est_civil = input("ingrese estado civil soltero = S o casado = C: ")
donde_vive = input("ingrese si vive en urbano = U o en rural = R: ")
if año_perten > 10 and num_hijos >= 2:
    print("APROBADO")
else:
    if est_civil == "C" and num_hijos > 3 and 1965 <= edad <= 1975:
        print("APROBADO")
    else:
        if ingreso > 2500000 and est_civil == "S" and donde_vive == "U":
            print("APROBADO")
        else:
            if ingreso > 3500000 and año_perten > 5:
                print("APROBADO")
            else:
                if donde_vive == "R" and est_civil == "C" and 0 < num_hijos < 2:
                    print("APROBADO")
                else:
                    print("RECHAZO")   
