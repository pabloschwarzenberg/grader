pesos = eval(input("Ingreso:"))
años = eval(input("Año de nacimiento:"))
hijos = eval(input("Numero de hijos:"))
años2 = eval(input("Años de pertenencia al banco:"))
civil= str(input("Estado civil"))
vivir = str(input("vive en campo o ciudad(u o r):"))
años_a= (años - 2020) * -1 
if hijos>=2 and años2 >10:
    print("APROBADO")
else:
    if hijos>3 and 55>=años_a>=45:
        print("APROBADO")
    else:
        if 2500000>pesos and civil =="S" and vivir =="U":
            print("APROBADO")
        else:
            if 3500000>pesos and años2>5:
                print("APROBADO")
            else:
                if vivir == "R" and civil =="C" and hijos<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
          
