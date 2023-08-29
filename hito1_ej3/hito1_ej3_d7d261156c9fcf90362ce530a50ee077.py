#Aprobación de créditos
ingreso=int(input("ingreso:"))
nacimiento=int(input("año nacimiento"))
hijos=int(input("número de hijos"))
banco=int(input("años de pertenencia al banco"))
estadocivil=input("estado civil")
campociudad=input("campo/ciudad")
edad=int(2018-nacimiento)
if banco>10 and hijos>=2:
    print("APROBADO")
else:
    if estadocivil=="C" and hijos>3 and 45<edad>55:
        print("APROBADO")
    else:
        if ingreso>2500000 and estadocivil=="S" and campociudad=="U":
           print("APROBADO")
        else:
            if ingreso>3500000 and banco>5:
                print("APROBADO")
            else:
                if campociudad=="R" and estadocivil=="C" and hijos<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")      