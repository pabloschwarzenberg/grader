print("¿Su credito es aprobado?")
ingreso= eval(input("Ingrese cantidad de ingresos:"))
año= eval(input("Ingrese año de nacimiento:"))
nhijos= eval(input("Ingrese cantidad de hijos/as:"))
añosbanco= eval(input("Ingrese cuantos años pertenece a este banco:"))
ecivil= str(input("Ingrese estado civil (S/C):"))
localidad= str(input("Ingrese si vive en campo o ciudad (U/R):"))
edad= 2020- año
if añosbanco>=10 and nhijos>=2:
    print("Su crédito fue APROBADO")
else:
    if ecivil == "C" and nhijos>3 and edad>=45 and edad<=55:
        print("Su crédito fue APROBADO")
    else:
        if ingreso>2500000 and ecivil == "S" and localidad == "U":
            print("Su crédito fue APROBADO")
        else:
            if ingreso>3500000 and añosbanco>5:
                print("Su crédito fue APROBADO")
            else:
                if localidad== "R" and ecivil == "C" and nhijos<2:
                    print("Su crédito fue APROBADO")
                else:
                    print("Su crédito fue RECHAZADO")

      