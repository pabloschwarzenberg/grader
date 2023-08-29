ingreso = int(input("Ingreso(en pesos): "))
año_nacimiento = int(input("Ingrese año de nacimiento: "))
n_hijos = int(input("Ingrese numeros de hijos: "))            
año_banco = int(input("Ingrese año de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil(*S*: soltero , *C*: casado): ")
vivienda = input("Ingrese su tipo de vivienda(*U*:urbano , *R*:rural: ")
#SI SE CUMPLE 1 DE ELLAS, ENTONCES APRUEBA

edad = 2021 - año_nacimiento

if(año_banco > 10 and n_hijos >= 2):
    print("APROBADO")

else:
    if(estado_civil == "C" and n_hijos > 3 and edad >= 45 and edad <= 55):
        print("APROBADO")

    else:
        if(ingreso > 2500000 and estado_civil == "S" and vivienda == "U"):
            print("APROBADO")

        else:
            if(ingreso > 3500000 and año_banco > 5):
                print("APROBADO")

            else:
                if(vivienda == "R" and estado_civil == "C" and n_hijos < 2):
                    print("APROBADO")

                else:
                    print("RECHAZADO")
      