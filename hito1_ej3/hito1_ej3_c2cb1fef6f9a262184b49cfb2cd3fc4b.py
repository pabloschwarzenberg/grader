ingr = int(input("Ingrese sus ingresos en pesos: "))
naci = int(input("Año completo de Nacimiento: "))
edad = (2021 - naci)
hijo = int(input("Cantidad de hijos: "))
banc = int(input("Año en el banco: "))
civi = input("Solter/Casado S/C: ")
vivi = input("Urbano/Rural U/R: ")

if banc > 10 and hijo >= 2:
    print("APROBADO")
elif civi == "C" and hijo > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingr > 2500000 and civi == "S" and vivi == "U":
    print("APROBADO")
elif ingr > 3500000 and banc > 5:
    print("APROBADO")
elif civi == "C" and hijo < 2 and vivi == "R":
    print("APROBADO")
else:
    print("RECHAZADO")