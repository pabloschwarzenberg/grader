#Aprobación de créditos
ing = int(input("Ingreso: "))
nacimiento = int(input("Año de nacimiento: "))
ninos = int(input("Numero de hijos: "))
bank = int(input("Años de pertenencia al banco: "))
Estado= input("Estado civil (S: soltero, C: casado): ")
hogar = input("En que lugar vives? (U: Urbano, R: Rural): ")

if (bank > 10 and ninos > 2):
    print("APROBADO")
    if (bank < 10 and ninos < 2) :
        print("RECHAZADO")

if (Estado == "C" and ninos > 3 and nacimiento >= 1976 or nacimiento <= 1966):
        print("APROBADO")
        if (Estado  == "S" and ninos < 3 and nacimiento <= 1976 or nacimiento >= 1966):
                print("RECHAZADO")

if (ing > 2500000 and Estado == "S" and hogar == "U"):
    print("APROBADO")
    if (ing < 2500000 and Estado == "C" and hogar == "R"):
           print("RECHAZADO")

if (ing > 3500000 and bank > 5):
    print("APROBADO")
    if(ing < 3500000 and bank < 5):
            print("RECHAZADO")

if (hogar == "R" and Estado == "C" and ninos < 2):
    print("APROBADO")
    if (hogar == "R" and Estado == "S" and ninos > 2):
        print("RECHAZADO")      