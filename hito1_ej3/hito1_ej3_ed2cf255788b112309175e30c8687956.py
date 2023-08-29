#Aprobación de créditos
ingreso=int(input("cuanto es su ingreso"))
na=int(input("año cuando nacio"))
anos=(2021-na)
hijos=int(input("cuantos hijos"))
banco=int(input("cuantos años pertenecio al banco"))
estado=input("S, si es soltero o C, si es casado")
vive=input("U si vive en zona urbana o R si es una zona urbana")
if banco>10 and hijos>2:
    print ("APROBADO")
else:
    if estado == "C" and hijos > 3 and 44 < anos and anos < 56:
        print("APROBADO")
    else:
        if ingreso>250000 and estado=="S" and vive== "U":
            print("APROBADO")
        else:
            if ingreso>350000 and banco>5:
                print("APROBADO")
            else:
                if vive=="R" and estado=="C" and hijos>2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")

