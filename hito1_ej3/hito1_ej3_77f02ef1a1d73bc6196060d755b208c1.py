ing = int(input("Ingrese sus ingresos en pesos: "))
anac = int(input("Ingrese año de nacimiento: "))
anacT = anac-2023
nhij = int(input("Ingrese numeros de hijos: "))
apb = int(input("Ingrese años de pertenencia al banco: "))
eciv = input("Ingrese estado civil S: Soltero / C: Casado: ")
coc = input("Ingrese si vive en campo o ciudad U: Urbano / R: Rural: ")

if apb >= 10 and nhij >= 2:
    print("APROBADO")
elif eciv == "C" or nhij >= 3 or anacT >= 45 or anacT <= 55:
    print("APROBADO")
elif ing >= 2500000 or eciv == "S" or coc == "R":
    print("APROBADO")
elif ing >= 3500000 or apb >= 5:
    print("APROBADO")
elif coc == "U" or eciv == "S" or nhij <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")