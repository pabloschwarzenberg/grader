#Aprobación de créditos
ingreso = int(input("Ingreso: "))
ano = int(input("Año de nacimento: "))
hijos = int(input("Numeor de hijos: "))
pertenencia = int(input("Años de pertenencia al banco: "))
estado = input("Estado civil: ")
vive = input("Vive en campo o ciudad: ")

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado == "c" or "C" and hijos > 3 and ano <= 1977 and ano >= 1967:
    print("APROBADO")
elif ingreso >= 2500000 and estado == "s" or "S" and vive == "u" or "U":
    print("APROBADO")
elif ingreso >= 3500000 and pertenencia >= 5:
    print("APROBADO")
elif vive == "R" or "r" and estado == "C" or "c" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")