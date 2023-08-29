ingreso=input("Escriba su ingrese en pesos chilenos: ")
ingreso=int(ingreso)
año_de_nacimiento=input("ingrese su año de nacimiento: ")
año_de_nacimiento=int(año_de_nacimiento)
numero_de_hijos=input("ingrese numero de hijos: ")
numero_de_hijos=int(numero_de_hijos)
Años_de_pertenencia_al_banco=input("¿Cuantos años lleva en este banco? ")
Años_de_pertenencia_al_banco=int(Años_de_pertenencia_al_banco)
Estado_civil=input("Estado civil: ")
lugar_de_residencia=input("¿Vive en sector urbano o crural?: ")
Credito_Aprovado=False
if Años_de_pertenencia_al_banco>10 and numero_de_hijos>=2:
    Credito_Aprovado=True
    print("APROBADO")
if ingreso>2500000 and Estado_civil=="S" and lugar_de_residencia=="U":
    Credito_Aprovado=True
    print("APROBADO")
if ingreso>3500000 and Años_de_pertenencia_al_banco>5:
    Credito_Aprovado=True
    print("APROBADO")
if lugar_de_residencia=="R" and Estado_civil=="C" and numero_de_hijos<2:
    Credito_Aprovado=True
    print("APROBADO")
if Estado_civil=="C" and numero_de_hijos>3 and 55>=2017-año_de_nacimiento and 2017-año_de_nacimiento>45:
    Credito_Aprovado=True
    print("APROBADO")
if Credito_Aprovado==False:
    print("RECHAZADO")