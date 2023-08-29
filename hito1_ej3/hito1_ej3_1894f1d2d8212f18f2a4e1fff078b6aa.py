#Aprobación de créditos
monedinero = int(input("Ingreso: "))
nacimiento = int(input("Año de nacimiento: "))
Hijos = int(input("Numero de hijos: "))
BANCO = int(input("Años de pertenencia al banco: "))
Estado= input("Estado civil (S: soltero, C: casado): ")
lugarespaciotiempo = input("En que lugar vives? (U: Urbano, R: Rural): ")

if (BANCO > 10 and Hijos > 2):
    print("APROBADO")
    if (BANCO < 10 and Hijos < 2) :
        print("RECHAZADO")

if (Estado == "C" and Hijos > 3 and nacimiento >= 1976 or nacimiento <= 1966):
        print("APROBADO")
        if (Estado  == "S" and Hijos < 3 and nacimiento <= 1976 or nacimiento >= 1966):
                print("RECHAZADO")

if (monedinero > 2500000 and Estado == "S" and lugarespaciotiempo == "U"):
    print("APROBADO")
    if (monedinero < 2500000 and Estado == "C" and lugarespaciotiempo == "R"):
           print("RECHAZADO")

if (monedinero > 3500000 and BANCO > 5):
    print("APROBADO")
    if(monedinero < 3500000 and BANCO < 5):
            print("RECHAZADO")

if (lugarespaciotiempo == "R" and Estado == "C" and Hijos < 2):
    print("APROBADO")
    if (lugarespaciotiempo == "R" and Estado == "S" and Hijos > 2):
        print("RECHAZADO")