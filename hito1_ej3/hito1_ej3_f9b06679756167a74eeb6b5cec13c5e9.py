#Aprobación de créditos
IN = int(input("Ingrese el ingreso en pesos: "))
AN = int(input("Ingrese su año de nacimiento: "))
NH = int(input("Ingrese cuantos hjos tiene: "))
AP = int(input("Años de pertenencia al banco: "))
EC = str(input("Ingrese su estado civil: S si está soltero o C si está casado: "))
V = str(input("Ingrese lugar donde vive: U si vive en lugar urbano o R si viven en lugar rural: "))
edad = 2020 - AN
if (AP>= 10) and (NH>=2):
    print("APROBADO")
elif (EC == "C") and (NH>3) and (45<=edad>=55):
    print("APROBADO")
elif (IN>=2500000) and (EC == "S") and (V == "U"):
    print("APROBADO")
elif (IN>=35000000) and (AP>=5):
    print("APROBADO")
elif (V == "R") and (EC == "C") and (NH<2):
    print("APROBADO")
else:
    print("RECHAZADO")