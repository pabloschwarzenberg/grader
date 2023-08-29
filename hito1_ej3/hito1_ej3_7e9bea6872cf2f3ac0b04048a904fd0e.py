ingreso=float(input("ingrese monto en pesos: "))
año_nacimiento=int(input("ingrese año de nacimiento: "))
edad=2021-año_nacimiento
numero_hijos=int(input("ingrese numero de hijos: "))
añodeper=int(input("ingrese año los años de pertenencia al banco: " ))
estado=input("ingrese estado civil (S: soltero| C: casado): ")
vivienda=input("ingrese donde vive (U: urbano| R: rural): ")
if añodeper>10 and numero_hijos>=2:
    print("APROBADO")
else:
    if(estado== "c" or estado == "C") and numero_hijos > 3 and (edad>45 and edad<55):
        print("APROBADO")
    else:

        if ingreso > 2500000 and (estado=="s" or estado=="S") and (vivienda == "U" or estado == "U"):
            print("APROBADO")
        else:
            print("APROBADO")