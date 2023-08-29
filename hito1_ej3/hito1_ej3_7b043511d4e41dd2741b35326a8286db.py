income = int(input("Ingreso laboral (en pesos): "))
year = int(input("Ingrese su año de nacimiento: "))
kids = int(input("Ingrese la cantidad de hijos: "))
loyalty = int(input("Ingrese cuantos años lleva operando con nosotros: "))
civil = str(input("Ingrese su estado civil ('S': soltero, 'C', casado): "))
location = str(input("Ingrese acorde si vive en campo o cuidad ('U': urbano, 'R': rural): "))
age = 2020 - year
if(len(str(civil)) == 1 and len(location) == 1 and len(str(year)) == 4):
    if(civil == "S" or civil == "C" or civil == "s" or civil == "c"):
        if(location == "U" or location == "R" or location == "u" or location == "r"):
            if(loyalty > 10 and kids >= 2):
                print("APROBADO")
            elif(civil == "C" and kids > 3 and 55>=age>=45):
                print("APROBADO")
            elif(income > 2500000 and (civil == "S" or civil == "s") and (location == "U" or location == "u")):
                print("APROBADO")
            elif(income > 3500000 and loyalty > 5):
                print("APROBADO")
            elif((location == "R" or location == "r") and (civil == "C" or civil == "c") and kids < 2):
                print("APROBADO")
            else:
                print("RECHAZADO")
        else:
            print("Por favor ingrese los datos de nuevo, su localizacion de campo o ciudad no es correcta")
    else:
        print("Datos ingresados no validos, intente nuevamente")
else:
    print("Datos ingresados no validos, intente nuevamente")