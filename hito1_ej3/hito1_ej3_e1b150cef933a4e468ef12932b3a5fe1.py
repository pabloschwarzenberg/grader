ing = int(input("coloque sus ingresos: "))
a_nacimiento = int(input("ingrese su año de nacimiento: "))
cantidad_hijos = int(input("¿cuantos hijos o hijas tiene usted?: "))
a_pertenencia_al_banco=int(input("ingrese sus años de pertenencia al banco: "))
estado_civil=str(input("ingrese su estado civil, s si es soltero y c si es casado: "))
lugar=str(input("ingrese donde vive, u si es un lugar urbano y r si es un lugar rural" ))

if a_pertenencia_al_banco>10 and cantidad_hijos>=2:
  print("APROBADO")
else:
    if estado_civil== "C" and cantidad_hijos>3 and 1975<a_nacimiento<1985:
        print("APROBADO")
    else:
        if ing>2500000 and estado_civil == "S" and lugar == "U":
            print("APROBADO")
        else:
            if ing>35000000 and a_pertenencia_al_banco>5:
                print("APROBADO")
            else:
                if lugar == "R" and estado_civil == "C" and cantidad_hijos<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")