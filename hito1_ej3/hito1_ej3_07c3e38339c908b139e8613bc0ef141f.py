Ingr= int(input("Ingrese su ingreso en pesos: "))
AgnoNac= int(input("Ingrese su año de nacimiento: "))
NumH= int(input("Ingrese su numero de hijos: "))
AgnosPB= int(input("Ingrese su numero de años de pertenencia al banco: "))
EstCiv= input("Ingrese 'C' si es casado o 'S' si es soltero: ")
CamCiu= input("Ingrese 'U' si vive en la ciudad o 'R' si vive en el campo: ")
Edad= int(2017-AgnoNac)


if (AgnosPB>10 and NumH>=2):
    print("APROBADO ")
else:
    if (EstCiv=="C" and NumH>3 and 45<Edad and Edad<55):
        print("APROBADO ")
    else:
        if (Ingr>2500000 and EstCiv=="S" and CamCiu=="U"):
            print("APROBADO ")
        else:
          if (CamCiu=="R" and EstCiv=="C" and 0<=NumH<2):
             print("APROBADO ")
          else:
            if (Ingr>3500000 and AgnosPB>5):
              print("APROBADO ")
            else:
              print("RECHAZADO ")
