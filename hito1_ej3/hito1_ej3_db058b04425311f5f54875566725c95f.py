#Aprobación de créditos
ingreso=int(input("Ingreso: "))
born=int(input("Año de nacimiento: "))
Hijos=int(input("Numero de hijos: "))
banco=int(input("Años de pertenencia al banco: "))
Estado=input("Estado civil (""S"": soltero, ""C"":casado): ")
Vivienda=input("En que lugar vives? (""U"":Urbano, ""R"":Rural): ")

if (banco > 10 and Hijos > 2):
        print("APROBADO")
        if (banco< 10 and Hijos < 2):
                 print("RECHAZADO")

if (Estado == 'C' or 'c' and Hijos > 3 and born >1976 or born  <1966):
    print("APROBADO")
    if (Estado == 'S' or 's' and Hijos < 3 and born < 1976 or born >1966):
            print("RECHAZADO")

if (ingreso > 2500000 and Estado == 'S' or 's' and Vivienda == 'U' or 'u'):
    print("APROBADO")
    if (ingreso < 2500000 and Estado == 'C' or 'c' and Vivienda == 'R' or 'r'):
           print("RECHAZADO")

if (ingreso > 3500000 and banco > 5):
    print("APROBADO")
    if(ingreso < 3500000 and banco < 5):
            print("RECHAZADO")

if (Vivienda == 'R' or 'r' and Estado == 'C'or 'c' and Hijos < 2):
    print("APROBADO")
    if(Vivienda == 'U' or 'u' and Estado == 's' or 'S' and Hijos > 2):
        print("RECHAZADO")

