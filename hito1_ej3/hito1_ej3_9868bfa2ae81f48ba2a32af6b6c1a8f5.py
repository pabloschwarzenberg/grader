#Aprobación de créditos
dinero = int(input("ingresos: "))
nacimiento = int(input("Año de nacimiento: "))
numHijos = int(input("Ingrese numero de hijos: "))
banco = int(input("Años de pertenencia al banco: "))
estCiv = input("'S':soltero,'C':casado...:")
vivienda = input("'U': urbano, 'R': rural")
anos = 2020-nacimiento
if banco > 10 and numHijos>=2:
    print("APROBADO")
elif estCiv == "C" or "c" and numHijos>3 and anos>=45 and anos<=55:
    print("APROBADO")
elif dinero > 2500000 and estCiv == "S" or "s" and vivienda == "U" or "u":
    print("APROBADO")
elif dinero > 3500000 and banco>5:
    print("APROBADO")
elif vivienda == "R" or "r" and estCiv == "S" or "s" and numHijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")      