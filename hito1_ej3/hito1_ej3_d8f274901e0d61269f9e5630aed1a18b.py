#Aprobación de créditos
pesos = int(input("Ingrese su sueldo mensual: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
Hijos = int(input("Ingrese el numero de hijos: "))
Pertenencia = int(input("Ingrese los años de pertenencia al banco: "))

#if civil else no civil
civil = input("Ingrese su estado civil(S: Soltero, C: Casado): ")

#Si vive en campo o ciudad
vive = input("Ingrese su tipo de lugar de residencia(U: Urbano, R: Rural): ")

#Aprobacion de creditos
if Pertenencia > 10 and Hijos > 1:
    print("APROBADO")

else:
    if civil == "C" or civil == "c" and Hijos > 3 and nacimiento > 1965 and nacimiento < 1977:
        print("APROBADO")

    else:
        if pesos > 2500000 and civil == "S" and vive == "U":
            print("APROBADO")
            
        else:
            if pesos > 2500000 and civil == "s" and vive == "u":
                print("APROBADO")

            else:
                if pesos > 3500000 and Pertenencia > 5:
                    print("APROBADO")

                else:
                    if vive =="R" and civil == "C" and Hijos < 2:
                        print("APROBADO")

                    else:
                        if vive =="r" and civil == "c" and Hijos < 2:
                            print("APROBADO")

                        else:
                            print("RECHAZADO")
