ingresos= int(input("Ingrese el monto de sus ingresos: "))
añoNac= input("Ingrese el año de nacimiento: ")
edad= 2020- eval(añoNac)
nHijos= int(input("Ingrese el numero de hijos:"))
antigued= int(input("Ingrese los años de pertenencia en el banco:"))
estadoCivil=input("Ingrese el estado civil: S para soltero o C para casado: ")
urbano=input("Ingrese el tipo de ciudad: U para Urbano y R para rural: ")

if((antigued>10)and(nHijos>=2)):
    print("CREDITO APROBADO")
else:
    if((estadoCivil=="C")and(nHijos>3)and(edad>=45 and edad<=55)):
        print("CREDITO APROBADO")
    else:
        if((ingresos>2500000)and(estadoCivil=="S")and(urbano=="U")):
            print("CREDITO APROBADO")
        else:
            if((ingresos>3500000)and(antigued>5)):
                print("CREDITO APROBADO")
            else:
                if((urbano=="R")and(estadoCivil=="C")and(nHijos<2)):
                    print("CREDITO APROBADO")
                else:
                    print("CREDITO NO APROBADO")