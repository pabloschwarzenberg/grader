#Aprobación de créditos
ingreso=int(input())
año=int(input())
hijos=int(input())
pertenencia=int(input())
estado=input("si es casado ponga C si es soltero ponga S")
vive=input("si vive en la ciudad ponga U, si vive en el campo ponga R")


if pertenencia>10 and hijos>=2:
    print("APROBADO")
else:
    if estado=="C" and hijos>3 and 1963<=año<=1973:
        print("APROBADO")
    else:
        if ingreso>2500000 and estado=="S" and vive=="U":
            print("APROBADO")
        else:
            if ingreso>3500000 and pertenencia>5:
                print("APROBADO")
            else:
                if vive=="R" and estado=="C" and hijos<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")

