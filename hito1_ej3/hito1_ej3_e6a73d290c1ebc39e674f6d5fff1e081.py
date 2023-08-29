#Aprobación de créditos
ingresos = int(input("Ingresos (en pesos): "))
ano = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos: "))
tiempo = int(input("Ingrese cuantos años lleva operando con nosotros: "))
estadocivil = str(input("Ingrese su estado civil ('S': soltero, 'C', casado): "))
localidad = str(input("Ingrese acorde si vive en campo o cuidad ('U': urbano, 'R': rural): "))
edad = 2020 - ano
if(len(str(estadocivil)) == 1 and len(localidad) == 1 and len(str(ano)) == 4):
    if(estadocivil == "S" or estadocivil == "C" or estadocivil == "s" or estadocivil == "c"):
        if(localidad == "U" or localidad == "R" or localidad == "u" or localidad == "r"):
            if(tiempo > 10 and hijos >= 2):
                print("APROBADO")
            elif(estadocivil == "C" and hijos > 3 and 55>=edad>=45):
                print("APROBADO")
            elif(ingresos > 2500000 and (estadocivil == "S" or estadocivil == "s") and (localidad == "U" or localidad == "u")):
                print("APROBADO")
            elif(ingresos > 3500000 and tiempo > 5):
                print("APROBADO")
            elif((localidad == "R" or localidad == "r") and (estadocivil == "C" or estadocivil == "c") and hijos < 2):
                print("APROBADO")
            else:
                print("RECHAZADO")
        else:
            print("ingrese los datos de nuevo, su localizacion de campo o ciudad es incorrecta")
    else:
        print("Datos ingresados no validos, intente nuevamente")
else:
    print("Datos ingresados no validos, intente nuevamente")     