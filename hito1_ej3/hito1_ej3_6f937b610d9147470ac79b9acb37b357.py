#Aprobación de créditos
I=int(input("Colocar ingreso en pesos: "))
AN=int(input("Colocar año de nacimiento: "))
NH=int(input("Colocar número de hijos: "))
AB=int(input("Colocar años de pertenencia al Banco: "))
EC=input("colocar Estado Civil (S=Soltero, C=Casado): ")
VV=input("Campo o ciudad (U=Urbano, R=Rural): ")
if 10<AB:
    if 2<=NH:
        print("APROBADO")
    else:
        print("RECHAZADO")
if EC == "C":
    if 3<NH:
        if 1965<=AN<=1975:
            print("APROBADO")
        else:
            print("RECHAZADO")
    else:
        print("RECHAZADO")
if 2500000<I:
    if EC == "S":
        if VV == "U":
            print("APROBADO")
        else:
            print("RECHAZADO")
    else:
        print("RECHAZADO")
if 3500000<I:
    if 5<AB:
        print("APROBADO")
    else:
        print("RECHAZADO")
if VV == "R":
    if EC == "C":
        if NH<2:
            print("APROBADO")
        else:
            print("RECHAZADO")
    else:
        print("RECHAZADO")