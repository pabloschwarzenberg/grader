dinero= int(input("ingrese sus ingresos monetarios: "))
nacimiento=int(input("ingrese su año de nacimiento: "))
hijos=int(input("ingrese su numero de hijos: "))
anos=int(input("ingrese sus años en el banco: "))
civil=(input("ingrese su estado civil, sabiendo que s es soltero y c casado: "))
v=(input("inserte si vive en el campo o  ciudad, u para urbano, r para rural: "))
a= (anos-2020)
if (anos > 10) and (hijos >= 2):
    print("APROBADO")
else:
    if (civil == "S") and (hijos>3) and (45>= a <=55):
        print("APROBADO")
    else:
        if (dinero>2500000) and (civil=="S") and (v=="U"):
            print("APROBADO")
        else:
            if (dinero>3500000) and (anos>5):
                print("APROBADO")
            else:
                if (v=="R") and (civil=="C") and (hijos<2):
                    print("APROBADO")
                else:
                    print("RECHAZADO")     