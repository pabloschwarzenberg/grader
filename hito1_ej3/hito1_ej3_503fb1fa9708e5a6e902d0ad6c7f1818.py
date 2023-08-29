ingresos= int(input("Ingrese sus Ingresos (en pesos): "))
año= int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cantidad de hijos: "))
banco= int(input("Ingrese años de pertenencia al banco: "))
estado= input("Cual es su estado civil? (C) o (S): ")
vive= input("Vive en campo o ciudad? (U) O (R): ")

if año >= 10 and hijos >= 2:   
    print("APROBADO")
elif estado == "C" and hijos >= 3 and año >= 1977 and año <= 1987:
    print ("APROBRADO")
elif ingresos >= 2500000 and estado == "S" and vive == "U":
    print("APROBADO")
elif ingresos >= 3500000 and banco >= 5:
    print ("APROBADO")
elif vive == "R" and estado == "C" and hijos <= 2:
    print ("APROBADO")
else:
    print("RECHAZADO")