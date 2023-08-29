ingr = eval(input("Ingrese sus ingresos en pesos: "))
naci = eval(input("Año completo de Nacimiento: "))
edad = (2020 - naci)
hijo = eval(input("Cantidad de hijos: "))
banc = eval(input("Año en el banco: "))
civi = input("Solter/Casado S/C: ")
vivi = input("Urbano/Rural U/R: ")

#Primera
if banc >= 10 and hijo >= 2:
    print("APROBADO")
#Segunda
if civi == "C" and hijo > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
#Tercera
if ingr > 2500000 and civi == "S" and vivi == "U":
    print("APROBADO")
#Cuarta
if ingr > 3500000 and banc > 5:
    print("APROBADO")
#Quinta
if vivi == "R" and civi == "C" and hijo < 2:
    print("APROBADO")
else:print("RECHAZADO")