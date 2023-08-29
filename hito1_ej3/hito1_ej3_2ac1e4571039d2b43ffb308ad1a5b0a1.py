i= int(input("Su ingreso en pesos: "))
an= int(input("Ano de nacimiento: "))
h= int(input("Ingrese el numero de hijos: "))
ap= int(input("Ingrese los años de pertenecia al banco: "))
ec= str(input("Ingrese su estado civil(S o C): "))
uor= str(input("Ingrese si vive en zona Urbana o Rural (U o R ): "))

if (10 < ap) and (2 <= h):
    print("APROBADO")
elif (ec == "C") and (3 < h) and (1965 < an < 1977):
    print("APROBADO")
elif (uor == "R") and (ec == "C") and (h < 2):
    print("APROBADO")
elif (3500000 < i) and (5 < ap):
    print("APROBADO")
elif(2500000 < i)and (ec == "S")and (uor == "U"):
    print("APROBADO")

else:
    print("RECHAZADO")